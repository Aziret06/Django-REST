from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import (
    Director,
    Movie,
    Review
)


class DirectorsSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        movies = director.movies.count()
        return movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title duration director reviews'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class MoviesReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()

    def get_rating(self, movie):
        data = movie.reviews.all()
        return round(sum(i.stars for i in data) / len(data), 1)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=350)
    description = serializers.CharField(required=False, default='No description')
    duration = serializers.CharField(required=False)
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except:
            raise ValidationError('Director does not exist!')
        return director_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(min_value=1, max_value=5, default=5)
    movie_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except:
            raise ValidationError('Movie does not exist!')
        return movie_id
