from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world")
    else:
        return HttpResponse("Hello " + name)

def home(request):
    latest_movies = Movie.objects.all().order_by("-release_date")[:5] #ordena por orden descendente por el campo release date.
                                                                  #  Fijarse que pone un menos. Si queremos por ordes ascendiente se pone sin el menos

    context = {'movies': latest_movies}
    return render(request, "home.html",context)
