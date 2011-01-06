from django.http import HttpResponse

def _respond(code):
    return HttpResponse("{response: '%s'}" % code, mimetype = "text/javascript")
