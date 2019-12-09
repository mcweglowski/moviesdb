from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Movies Site!</h1>')
