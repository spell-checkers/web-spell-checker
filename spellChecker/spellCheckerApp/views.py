from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to our Web-Based Spell Checker:)")
