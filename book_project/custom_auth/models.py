from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
 
# Create your models here.

class UserManager(BaseUserManager):

    # Create a normal User 
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("User must have an valid email address")

        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    # Create a super user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
 
        return self.create_user(email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254,unique=True)
    city = models.CharField(max_length=254,blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    
    objects = UserManager()

    def __str__(self):
        return self.email
    