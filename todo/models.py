from django.db import models
from tv_show.models import FilmModel

class TodoModel(models.Model):
    STATUS_CHOICES = (
        ('Просмотрел', 'Просмотрел'),
        ('Не просмотрел', 'Не просмотрел'),
    )
    task = models.CharField(max_length=100)
    choice_film = models.ForeignKey(FilmModel, on_delete=models.CASCADE)
    choice_status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task