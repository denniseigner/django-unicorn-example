from django.conf import settings


def my_flag(request):
    return {"MY_FLAG": settings.MY_FLAG}
