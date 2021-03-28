from django.db import models
from django.contrib.auth.models import User

class AccountHolder(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return self.user.username