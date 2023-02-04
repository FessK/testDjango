from django.db import models


# Create your models here.
class Director(models.Model):
    pos_work = models.CharField(max_length=15, blank=False, default='director')
    name = models.CharField(max_length=20, blank=False, default='Test')
    second_name = models.CharField(max_length=20, blank=False, default='Testov')
    sur_name = models.CharField(max_length=20, blank=False, default='Testovich')
    salary = models.IntegerField(default=10000)
    dateStartWork = models.DateField()


class Lead_Department(models.Model):
    pos = models.ForeignKey(Director, on_delete=models.PROTECT)
    pos_work = models.CharField(max_length=15, blank=False, default='lead')
    name = models.CharField(max_length=20, blank=False, default='test')
    second_name = models.CharField(max_length=20, blank=False, default='testov')
    sur_name = models.CharField(max_length=20, blank=False, default='testovich')
    salary = models.IntegerField(default=0)
    dateStartWork = models.DateField()


class Worker(models.Model):
    pos = models.ForeignKey(Lead_Department, on_delete=models.PROTECT)
    pos_work = models.CharField(max_length=15, blank=False, default='tester')
    name = models.CharField(max_length=20, blank=False, default='test')
    second_name = models.CharField(max_length=20, blank=False, default='testov')
    sur_name = models.CharField(max_length=20, blank=False, default='testovich')
    salary = models.IntegerField(default=0)
    dateStartWork = models.DateField()
