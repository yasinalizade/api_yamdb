from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('year', 'genre', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'text', 'title', 'score', 'pub_date'
    )
    search_fields = ('text',)
    list_filter = ('title', 'score')


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'review', 'title', 'text', 'pub_date'
    )
    search_fields = ('text',)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'first_name',
                    'last_name', 'email', 'role', 'bio'
                    )
    search_fields = ('text',)
    #  list_filter = ('username',)
    list_editable = ('role',)
    empty_value_display = '-пусто-'


admin.site.register(User, ReviewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
