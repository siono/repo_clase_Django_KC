from rest_framework import serializers

from movies.models import Movie


class MoviesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id","image","title"]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"
