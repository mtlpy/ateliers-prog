from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hello(request):
    if "nom" in request.GET:
        nom = request.GET["nom"]
        msg = "Salut " + nom + "!"
    else:
        msg = "Salut Montréal!"
    return HttpResponse(msg)
