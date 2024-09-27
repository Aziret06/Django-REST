from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorsListAPIView.as_view()),
    path('director/<int:id>/', views.DirectorsDetailAPIView.as_view()),
    path('movies/', views.MoviesListAPIView.as_view()),
    path('movie/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('reviews/', views.ReviewsListAPIView.as_view()),
    path('review/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('movies/reviews/', views.MoviesReviewsAPIView.as_view()),
]