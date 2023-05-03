from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Footballer(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    age = models.IntegerField()

    def _str_(self):
        return f"{self.name}:{self.age}:{self.price}"


class Statistics(models.Model):
    f_name = models.CharField(max_length=255)
    goal = models.IntegerField()
    assist = models.IntegerField()
    game = models.IntegerField()
    club = models.CharField(max_length=255)

    def _str_(self):
        return f"{self.f_name}:{self.game}:{self.assist}:{self.game}:{self.club}"


class Clubs(models.Model):
    c_name = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)

    def _str_(self):
        return f"{self.c_name}:{self.manager}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


