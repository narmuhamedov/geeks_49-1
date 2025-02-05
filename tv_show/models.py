from django.db import models

class FilmModel(models.Model):
    GENRE_CHOICES = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
    )
    image = models.ImageField(upload_to='films/', verbose_name='загрузите фото')
    title = models.CharField(max_length=100, verbose_name='укажите название фильма')
    description = models.TextField(verbose_name='укажите описание фильма', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=200)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='COMEDY',
                             verbose_name='выберите жанр')
    time = models.TimeField(verbose_name='укажите время просмотра')
    director = models.CharField(max_length=100, default='Иванов Иван')
    trailer = models.URLField(verbose_name='укажите ссылку из YOUTUBE')
    #video = models.FileField(upload_to='videos/',)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'






