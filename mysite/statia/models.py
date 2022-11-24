from django.db import models
from django.urls import reverse  # Новый импорт


class Post(models.Model):
    title = models.CharField('Заголовок статьи', max_length=100)
    content = models.TextField('Текст записи')
    author = models.CharField('Автор записи', max_length=100)
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='image/%Y')

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f'{self.title}, {self.author}'

    def get_absolute_url(self):  # новый метод
        return reverse('post_detail', args=[str(self.id)])
