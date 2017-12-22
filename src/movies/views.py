from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from movies.forms import MovieForm
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

def movie_detail(request, pk):
    possible_movies = Movie.objects.filter(pk=pk).select_related("category")  #Decimos a Django que nos traiga la consulta relacionada de la categoria haciendo solo una peticion con JOIN
    if len(possible_movies) == 0:
        #la longitud es 0 -> la pelicula no existe
        return render(request, "404.html", status = 404)
    else:
        movie = possible_movies[0]
        context = {'movie': movie }
        return render(request, "movie_detail.html", context)

class CreateMovieView(View):

    def get(self, request):
        form = MovieForm()
        return render(request, "movie_form.html", {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            #vaciamos el formulario
            form = MovieForm()
            url = reverse("movie_detail_page", args=[movie.pk]) #reverse genera url pasandole el tipo de URL
            message = "Movie created successfully!"
            message += '<a href="{0}">View</a>'.format(url)
            #enviamos mensaje de exito con un enlace a la pelicula que acabamos de cr
            messages.success(request, message)
        return render(request, "movie_form.html", {'form':form})