from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Cohort(models.Model):
    name = models.CharField(max_length=255, unique=True)
    graduation_date = models.DateField()


class Student(models.Model):
    cohort = models.ForeignKey(
        to=Cohort, on_delete=models.CASCADE, related_name="students"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    projects = models.ManyToManyField(to="Project", related_name="members")


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
