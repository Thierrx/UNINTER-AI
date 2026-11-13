
from playwright.sync_api import sync_playwright
from pathlib import Path

BRAVE_PATH = (
    r"C:\Program Files\BraveSoftware"
    r"\Brave-Browser\Application\brave.exe"
)

PROJETO = Path(__file__).resolve().parent.parent
PERFIL = PROJETO / "perfil_brave"

URL_ALVO = "https://univirtus.uninter.com/ava/web/#/ava"

NOME_DISCIPLINA = "Práticas em Sistemas Operacionais"
NOME_AULA = "Introdução aos Sistemas Operacionais GNU/Linux"


def abrir_brave():
    with sync_playwright() as playwright:
        contexto = playwright.chromium.launch_persistent_context(
            user_data_dir=str(PERFIL),
            executable_path=BRAVE_PATH,
            headless=False,
            viewport={"width": 1366, "height": 768}
        )

        pagina = contexto.pages[0] if contexto.pages else contexto.new_page()

        try:
            pagina.goto(URL_ALVO, wait_until="domcontentloaded")

            print("Entre no UNIVIRTUS e chegue à página inicial do AVA.")

            while pagina.url != URL_ALVO:
                pagina.wait_for_timeout(1000)

            input("Quando estiver no AVA, pressione ENTER aqui no CMD.")

            print("\nClique em MEUS CURSOS no Brave.")
            input("Quando as disciplinas aparecerem, pressione ENTER.")

            pagina.wait_for_timeout(3000)

            print("\n========== ABRINDO DISCIPLINA ==========")

            disciplina = pagina.locator("a:visible").filter(
                has_text=NOME_DISCIPLINA
            ).last

            disciplina.click()
            pagina.wait_for_timeout(5000)

            print("Disciplina aberta!")

            print("\n========== LOCALIZANDO AULA ==========")

            aula = pagina.locator(
                'a[href*="/ava/web/roa/?item="]'
            ).filter(has_text=NOME_AULA).first

            aula.wait_for(state="visible", timeout=15000)

            link_aula = aula.get_attribute("href")

            print("Aula encontrada!")

            print("\n========== ABRINDO CONTEÚDO ==========")

            pagina.goto(
                link_aula,
                wait_until="domcontentloaded"
            )

            pagina.wait_for_timeout(7000)

            print("\n========== LOCALIZANDO FRAME DO MATERIAL ==========")

            frame_aula = None

            for frame in pagina.frames:
                if "conteudosdigitais.uninter.com/libraries/newrota/" in frame.url:
                    frame_aula = frame
                    break

            if frame_aula is None:
                print("Frame do material não encontrado.")

                for frame in pagina.frames:
                    print("Frame disponível:", frame.url)

                raise Exception(
                    "Não foi possível localizar o material da aula."
                )

            print("Frame encontrado!")
            print("Endereço:", frame_aula.url)

            print("\n========== EXTRAINDO TEXTO ==========")

            frame_aula.locator("body").wait_for(
                state="attached",
                timeout=20000
            )

            pagina.wait_for_timeout(5000)

            conteudo = frame_aula.locator("body").inner_text()

            if not conteudo.strip():
                raise Exception("O conteúdo extraído está vazio.")

            print("\n========== TEXTO EXTRAÍDO ==========")
            print(conteudo)

            arquivo = PROJETO / "texto_aula.txt"

            arquivo.write_text(
                conteudo,
                encoding="utf-8"
            )

            print("\n========== EXTRAÇÃO CONCLUÍDA ==========")
            print("Caracteres extraídos:", len(conteudo))
            print("Texto salvo em:", arquivo)

        except Exception as erro:
            print("\nERRO DURANTE A LEITURA:")
            print(erro)

            print("\nFrames encontrados:")

            for frame in pagina.frames:
                print(frame.url)

        input("\nPressione ENTER para fechar...")
        contexto.close()


if __name__ == "__main__":
    abrir_brave()
