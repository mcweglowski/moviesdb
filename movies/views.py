from django.http import HttpResponse


def home(request):
    return HttpResponse(f'''<head>
                                <title>Movies DB</title>
                            </head>
                            <body>
                                <h1>Movies Site!</h1>
                            </body>''')
