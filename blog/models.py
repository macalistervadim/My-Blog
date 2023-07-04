from django.db import models

class Post(models.Model):
    """Данные о записи"""
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Автор', max_length=100)
    date_created = models.DateField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='image/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title} {self.author}'

class Comment(models.Model):
    """Коментарии к конкретной записи"""
    email = models.EmailField('Почтовый адрес')
    name = models.CharField('Имя',max_length=50)
    text_comment = models.TextField('Текст комментария', max_length=1000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name} {self.post}'
