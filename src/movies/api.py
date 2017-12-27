from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


from movies.models import Movie
from movies.serializers import MovieSerializer, MoviesListSerializer


#creamos el endpoint de creación y listado de peliculas utilizando listas genericas
class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()

    #como al crear una pelicula necesito que coja todos los campos nos redifinos la funcion
    def get_serializer_class(self):
        return MoviesListSerializer if self.request.method == "GET" else MovieSerializer #operador ternario

#endpoint actualización y eliminación
class MovieDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
