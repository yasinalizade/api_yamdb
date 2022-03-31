from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator


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
        # default=1, Не уверен, нужно ли дефолтное значение
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateField('Дата публикации', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}: {self.score}'


class Comment(models.Model):
    """Модель - комментарии."""
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

    def __str__(self) -> str:
        return f'{self.text[:20]}'


class User(AbstractUser):
    USER = 1
    MODERATOR = 2
    ADMIN = 3

    ROLE_CHOICES = (
          (USER, 'User'),
          (MODERATOR, 'Moderator'),
          (ADMIN, 'Admin'),
      )

    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=False)
    #  role = models.CharField(choices=ROLE_CHOICES, blank=True, null=False)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        'Username',
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        help_text=('Обязательное поле. Только буквы и цифры. До 150 символов'),
        validators=[username_validator],
        error_messages={
            'unique': ('Пользователь с таким именем уже зарегистрирован.')
        },
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        blank=False,
        unique=True,
        null=False
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=False
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=False
    )
    confirmation_code = models.CharField(max_length=6)
    role = models.CharField(
        'Роль',
        max_length=30,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )

    #  USERNAME_FIELD = 'email'
    #  REQUIRED_FIELD = ['confirmation_code']

    def __str__(self):
        return self.email
