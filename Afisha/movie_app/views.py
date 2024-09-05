from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from .models import (
    Director,
    Movie,
    Review
)

from .serializers import (
    DirectorsSerializer,
    MoviesSerializer,
    MovieDetailSerializer,
    ReviewSerializer
)


@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorsSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail_api_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = DirectorsSerializer(director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    data = MoviesSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = MovieDetailSerializer(movie, many=False).data
    return Response(data=data)


@api_view(['GET'])
def reviews_list_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = ReviewSerializer(review, many=False).data
    return Response(data=data)
