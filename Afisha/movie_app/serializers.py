from rest_framework import serializers

from .models import (
    Director,
    Movie,
    Review
)


class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title duration'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

