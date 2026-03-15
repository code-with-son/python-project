from django.db import models

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
