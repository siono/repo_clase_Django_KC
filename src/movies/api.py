from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response


from movies.models import Movie
from movies.serializers import MovieSerializer

#creamos el endpoint de creación y listado de peliculas utilizando listas genericas
class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer