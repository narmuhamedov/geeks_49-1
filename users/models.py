from django.db import models
from django.contrib.auth.models import User

child_club = 'Детский клуб'
teenager_club = 'Подростковый клуб'
adult_club = 'Взрослый клуб'

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14, default='+996')
    #важное для middlewares для проверки возраста
    age = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    club = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.age < 7:
            self.club = 'age must be at least 7'
        elif 7 <= self.age < 12:
            self.club = child_club
        elif 12 <= self.age < 18:
            self.club = teenager_club
        elif 18 <= self.age < 60:
            self.club = adult_club
        else:
            self.club = 'Вы слишком опытны вам это покажется скучным'
        super().save(*args, **kwargs)

