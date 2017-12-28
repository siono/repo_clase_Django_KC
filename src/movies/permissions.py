from rest_framework.permissions import BasePermission


class MoviesPermission(BasePermission):

    def has_permission(self, request, view):
        return request.method == "GET" or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method == "GET" or obj.user == request.user  #si el metodo es GET o si el usuario es propietario de la pelicula si puede acceder a ella


class CategoriesPermission(BasePermission):

    def has_permission(self, request, view):
        return request.method == "GET" or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.method == "GET" or request.user.is_superuser

