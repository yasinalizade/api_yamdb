from django.db import models

from .validators import validate_score


class Category(models.Model):
    """Модель - отзывы."""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель - жанры."""
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель - проивзедения."""
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    rating = models.PositiveIntegerField(blank=True)
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genre, related_name='titles')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    """Модель - отзывы."""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField
    # Здесь будет author
    score = models.IntegerField(
        'Поставьте оценку от 1 до 10',
        validators=[validate_score],
    )
    pub_date = models.DateField('Дата публикации', auto_now_add=True)


class Comment(models.Model):
    """Модель - коммантирии."""
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField
    # Здесь будет author
    pub_date = models.DateField('Дата публикации', auto_now_add=True)
