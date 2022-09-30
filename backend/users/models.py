from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    USER_ROLES = [(USER, 'User'), (ADMIN, 'Admin')]
    role = models.CharField(
        'Роль',
        max_length=20,
        choices=USER_ROLES,
        default=USER
    )

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        ordering = ('pk',)
