from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.directors_list_api_view),
    path('director/<int:id>/', views.director_detail_api_view),
    path('movies/', views.movies_list_api_view),
    path('movie/<int:id>/', views.movie_detail_api_view),
    path('reviews/', views.reviews_list_api_view),
    path('review/<int:id>/', views.review_detail_api_view),
    path('movies/reviews/', views.movies_reviews_api_view),
]