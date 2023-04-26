from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.first_name
    
    def isExists(self):
        if User.objects.filter(email = self.email):
            return True
        return False
    
    @staticmethod
    def get_customer_by_username(username):
        try:
            return User.objects.get(username = username)
        except:
            return False
