from django.db import models


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
