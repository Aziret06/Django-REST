from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

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
)


class DirectorsDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DirectorsSerializer
    queryset = Director.objects.all()
    lookup_field = 'id'


class DirectorsListAPIView(ListCreateAPIView):
    serializer_class = DirectorsSerializer
    queryset = Director.objects.all()
    pagination_class = PageNumberPagination


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MoviesSerializer
    queryset = Movie.objects.all()
    lookup_field = 'id'


class MoviesListAPIView(ListCreateAPIView):
    serializer_class = MoviesSerializer
    queryset = Movie.objects.all()


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'id'


class ReviewsListAPIView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class MoviesReviewsAPIView(ListCreateAPIView):
    serializer_class = MoviesReviewsSerializer
    queryset = Movie.objects.all()

