from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import (
    Director,
    Movie,
    Review
)

from .serializers import (
    DirectorsSerializer,
    MoviesSerializer,
    MovieDetailSerializer,
    ReviewSerializer,
    MoviesReviewsSerializer,
    MovieValidateSerializer,
    DirectorValidateSerializer,
    ReviewValidateSerializer
)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def directors_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorsSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
        director = Director.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=DirectorsSerializer(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorsSerializer(director, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=DirectorsSerializer(director).data)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movies_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MoviesSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )

        return Response(status=status.HTTP_201_CREATED,
                        data=MoviesSerializer(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieDetailSerializer(movie, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=MovieDetailSerializer(movie).data)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie_id')

        review = Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(review, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.movie_id = serializer.validated_data.get('movie_id')
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewSerializer(review).data)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movies_reviews_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MoviesReviewsSerializer(movies, many=True).data
        return Response(data=data)
