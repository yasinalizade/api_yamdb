from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'year', 'rating', 'description', 'genre', 'category'
    )
    search_fields = ('name',)
    list_filter = ('year', 'rating', 'genre', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'text', 'title', 'author', 'score', 'pub_date'
    )
    search_fields = ('text',)
    list_filter = ('title', 'score')


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'review', 'title', 'text', 'author', 'pub_date'
    )
    search_fields = ('text', 'author')
    list_filter = ('text',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
