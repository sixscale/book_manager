from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Books(models.Model):
    title = models.CharField(max_length=70)
    author = models.ManyToManyField
