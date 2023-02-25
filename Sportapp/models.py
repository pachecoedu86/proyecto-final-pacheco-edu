from django.db import models



class Sport(models.Model):

    def __str__(self):
        return f"Name: {self.name} ------ country: {self.country}"

    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class Player(models.Model):

    def __str__(self):
        return f"Name: {self.name} ---- Surname: {self.surname} ----- Age: {self.age} "

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age =  models.IntegerField()

class Coach(models.Model):

    def __str__(self):
        return f"Name: {self.name} --- Surname: {self.surname} -- Age: {self.age} --- Category: {self.category}"

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    category = models.CharField(max_length=30)   

class Team(models.Model):

    def __str__(self):
        return f"Name: {self.name} --- Country {self.country} ---- Host: {self.host} --- Championships: {self.Championships}"

    name = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    host = models.CharField(max_length=40)
    Championships = models.IntegerField()






