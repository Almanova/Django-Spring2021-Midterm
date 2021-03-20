from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from utils import constants


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, verbose_name='User')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email address')
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Last name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    role = models.CharField(choices=constants.ROLES, default=constants.GUEST, max_length=30, verbose_name='Role')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Profile')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name='User description')
    birthday = models.DateTimeField(blank=True, null=True, verbose_name='Birthday date')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
