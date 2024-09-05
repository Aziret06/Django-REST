from django.contrib import admin

from .models import (
    Director,
    Movie,
    Review
)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration')
    list_display_links = ('id', 'title', 'duration')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie')
    list_display_links = ('id', 'movie')
