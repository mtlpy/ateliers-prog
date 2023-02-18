from django.http import HttpResponse
from monsite.models import Book
from django.template.loader import get_template

# Create your views here.

def hello(request):
    if "nom" in request.GET:
        nom = request.GET["nom"]
        msg = "Salut " + nom + "!"
    else:
        msg = "Salut Montréal!"
    return HttpResponse(msg)



def homepage(request):
    template = get_template("homepage.html")
    context = {
        "title": "La liste de livres de ...",
        "pitch": "Les meilleurs livres sur Pyhon",
        "count": Book.objects.count(),
    }
    html = template.render(context)
    return HttpResponse(html)



def books(request):
    books = Book.objects.all()  # get all books from the DB
    template = get_template("books.html")
    context = {"books": books}
    html = template.render(context)
    return HttpResponse(html)



def bookdetails(request, book_id):
    book = Book.objects.get(id=book_id)
    template = get_template("bookdetails.html")
    context = {"book": book}
    html = template.render(context)
    return HttpResponse(html)
