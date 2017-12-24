from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from movies.forms import MovieForm
from movies.models import Movie


def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world")
    else:
        return HttpResponse("Hello " + name)

@login_required
def home(request):
    latest_movies = Movie.objects.all().order_by("-release_date")[:5] #ordena por orden descendente por el campo release date.
                                                                  #  Fijarse que pone un menos. Si queremos por ordes ascendiente se pone sin el menos

    context = {'movies': latest_movies}
    return render(request, "home.html",context)

@login_required
def movie_detail(request, pk):
    possible_movies = Movie.objects.filter(pk=pk).select_related("category")  #Decimos a Django que nos traiga la consulta relacionada de la categoria haciendo solo una peticion con JOIN
    if len(possible_movies) == 0:
        #la longitud es 0 -> la pelicula no existe
        return render(request, "404.html", status = 404)
    else:
        movie = possible_movies[0]
        context = {'movie': movie }
        return render(request, "movie_detail.html", context)


class CreateMovieView(LoginRequiredMixin,View):

    def get(self, request):
        form = MovieForm()
        return render(request, "movie_form.html", {'form': form})

    def post(self, request):
        movie = Movie()
        movie.user = request.user #asignamos a la pelicula el usuario autenticado
        form = MovieForm(request.POST, instance=movie) #le pasamos al movieForm la insatancia pelicula con el usuario autenticado
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

class MyMoviesView(ListView):

    model = Movie
    template_name = "my_movies.html"

    #como queremos filtrar solo por las peliculas que hemos creado con nuestro usuario redefinimos get_queryset ya que es la funcion que utiliza en el workflow de una listview : https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/
    def get_queryset(self):
        queryset = super(MyMoviesView,self).get_queryset() #llamamos
        return queryset.filter(user = self.request.user)