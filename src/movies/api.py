from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from movies.models import Movie, Category
from movies.permissions import MoviesPermission, CategoriesPermission
from movies.serializers import MovieSerializer, MoviesListSerializer, CategorySerializer


#creamos el endpoint de creación y listado de peliculas utilizando listas genericas
class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] #puede listar cualquier usuario pero solo puede crear peliculas los usuarios autenticados

    #como al crear una pelicula necesito que coja todos los campos nos redifinos la funcion
    def get_serializer_class(self):
        return MoviesListSerializer if self.request.method == "GET" else MovieSerializer #operador ternario

    #para que un usuario no pueda crear peliculas de otro usuario
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#endpoint actualización y eliminación
class MovieDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [MoviesPermission]

    # para que un usuario no pueda actualizar o borrar peliculas de otro usuario
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#endpoint para las categorias con ModelViewset
class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoriesPermission]

