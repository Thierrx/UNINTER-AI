
import subprocess
import sys

from pathlib import Path
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required(login_url="login")
def abrir_navegador(request):
    if request.method != "POST":
        return JsonResponse(
            {"erro": "Método não permitido."},
            status=405
        )

    projeto = Path(__file__).resolve().parent.parent
    script = projeto / "integrations" / "navegador.py"

    try:
        subprocess.Popen(
            [sys.executable, str(script)],
            cwd=str(projeto),
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

        return JsonResponse({
            "mensagem": "Brave iniciado com sucesso!"
        })

    except Exception:
        return JsonResponse({
            "erro": "Não foi possível abrir o Brave."
        }, status=500)
