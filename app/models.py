from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class Teachers(models.Model):
    full_name = models.CharField(max_length = 500)
    status = models.BooleanField(default = True)
    experience = models.CharField(max_length = 100)
    courses = models.ManyToManyField(Courses)

    def __str__(self) -> str:
        return self.full_name
    

class Students(models.Model):
    full_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 13)
    parents_phone_number = models.CharField(max_length = 13)
    telegram_link = models.CharField(max_length = 100)
    address = models.TextField()
    courses = models.ManyToManyField(Courses)
    teachers = models.ManyToManyField(Teachers)

    def __str__(self) -> str:
        return self.full_name
    
