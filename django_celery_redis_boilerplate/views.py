from django.http import JsonResponse


def health_check(request):
    # server health check
    try:
        # TODO: 연결된 DB 혹은 기타 서비스 상태 체크 로직
        return JsonResponse({"health_check": True})
    except Exception as exc:
        return JsonResponse({"health_check": False})
