from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator


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
