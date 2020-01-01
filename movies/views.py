from django.http import HttpResponse


def home(request):
    return HttpResponse(f'''<head>
                                <title>Movies DB</title>
                            </head>
                            <body>
                                <form id="testForm">Movies Site!</form>
                            </body>''')


def movies_get(request):
    pass


def movies_post(request):
    pass
