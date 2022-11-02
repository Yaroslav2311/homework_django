from django.db import models


class Cities(models.Model):
    citi = models.CharField(max_length=150)
    num_of_stores = models.IntegerField
    country = models.CharField(max_length=150, default='Ukraine')

    def __str__(self):
        return self.citi


class Client(models.Model):
    client = models.CharField(max_length=150)
    email = models.EmailField()
    cities = models.ForeignKey('Cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.client


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return self.name


class Providers(models.Model):
    provider_name = models.CharField(max_length=150)
    p_email = models.EmailField()
    cities = models.OneToOneField('Cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.provider_name


class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
