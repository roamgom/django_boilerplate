
from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin)
from django.db import models


class User(AbstractUser):

    phone_number = models.CharField(
        max_length=128, unique=True, blank=False, null=False)
