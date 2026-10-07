from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        creates and save a users with given email and password 
        """
        if not email:
            return ValueError('user must have a email')
        
        user = self.model(
            email=self.normalize_email(email)
        )
        
        user.set_password(password)
        user.save(using=self._db) 
        
        return user 
    
    def create_superuser(self, email, password=None):
            """
            creates and save a superuser with given email and password 
            """
            user = self.create_user(email, password=password)
            user.is_admin = True # super user
            user.save(using=self._db)
            
            return user 
        
        
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    phone_number= models.CharField(max_length=30)
    password = models.CharField(max_length=800)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    token_last_expired = models.DateTimeField(null=True) # auth 
    objects = MyUserManager() # laisson d'object 
    # it's obligation in exsit a model 
    USERNAME_FIELD = 'email' # default for django : connected for username or is connection for in  email 
    REQUIRED_FIELDS= [] # obligation for list vid
    
    class Meta :
        db_table = 'users'
        
    