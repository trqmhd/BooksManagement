from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from isbn_field import ISBNField
# Create your models here.


class UserProfileManager(BaseUserManager):
    def create_user (self, email, name, password = None):
        if not email:
            raise  ValueError ("User must have an email.")

        email = self.normalize_email(email)
        user = self.model(email= email, name = name)

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using= self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    name        = models.CharField(max_length= 255)
    email       = models.EmailField(max_length=255, unique=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

class BookStore(models.Model):
    title       = models.CharField(max_length=255)
    author      = models.CharField(max_length=255)
    isbn        = ISBNField(default=True)
    publication = models.CharField(max_length=255)
    created_on  = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
