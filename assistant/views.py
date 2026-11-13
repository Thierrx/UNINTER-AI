
from django.conf import settings
from django.http import JsonResponse
from google import genai
from google.genai import types


def perguntar_ia(request):
    if request.method != "POST":
        return JsonResponse(
            {"erro": "Método não permitido."},
            status=405
        )

    pergunta = request.POST.get("pergunta", "").strip()

    if not pergunta:
        return JsonResponse(
            {"erro": "Digite uma pergunta."},
            status=400
        )

    try:
        client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
            http_options=types.HttpOptions(timeout=20000)
        )

        resposta = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=pergunta
        )

        return JsonResponse({
            "resposta": resposta.text or "A IA não retornou texto."
        })

    except Exception as erro:
        erro_texto = str(erro).lower()

        if "503" in erro_texto or "unavailable" in erro_texto:
            return JsonResponse({
                "erro": "Gemini temporariamente sobrecarregado. Tente novamente."
            }, status=503)

        if "429" in erro_texto or "resource_exhausted" in erro_texto:
            return JsonResponse({
                "erro": "Limite de utilização da API atingido. Tente novamente mais tarde."
            }, status=429)

        if "timeout" in erro_texto or "timed out" in erro_texto:
            return JsonResponse({
                "erro": "O Gemini demorou demais para responder."
            }, status=504)

        return JsonResponse({
            "erro": "Não foi possível consultar o Gemini."
        }, status=500)
