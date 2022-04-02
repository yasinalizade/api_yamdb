from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from enum import Enum


class UserChoice(Enum):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )


class User(AbstractUser):
    """Модель - пользователи."""
    password = models.CharField(max_length=1, blank=True, null=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        'Пользователь',
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
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        'Роль',
        max_length=20,
        choices=[(tag.name, tag.value) for tag in UserChoice],
        default='user',
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
