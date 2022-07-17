from django.db import models

# Create your models here.


class AiClass(models.Model):
    class_num = models.IntegerField()
    teacher = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)
    students_num = models.IntegerField()


class AiStudent(models.Model):
    name = models.CharField(max_length=30)