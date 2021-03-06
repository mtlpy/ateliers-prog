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



from django.template.loader import get_template

def homepage(request):
    template = get_template("homepage.html")
    context = {
        "title": "La liste de livres de ...",
        "pitch": "Les meilleurs livres sur Pyhon",
    }
    html = template.render(context)
    return HttpResponse(html)


from monsite.models import Book


def books(request):
    books = Book.objects.all()  # get all books from the DB
    template = get_template("books.html")
    context = {"books": books}
    html = template.render(context)
    return HttpResponse(html)
