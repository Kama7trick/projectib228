from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=450)  # заголовок поста
    date = models.CharField(max_length=450)  # Дата
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста

    def __str__(self):  # Метод
        return self.title


class BirdPost(models.Model):
    title = models.CharField(max_length=450)  # Заголовок поста
    date = models.CharField(max_length=450)  # Дата
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста

    def __str__(self):  # Метод
        return self.title


class MammalsPost(models.Model):
    title = models.CharField(max_length=450)  # Заголовок поста
    date = models.CharField(max_length=450)  # Дата
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста

    def __str__(self):  # Метод
        return self.title


class FishPost(models.Model):
    title = models.CharField(max_length=450)  # Заголовок поста
    date = models.CharField(max_length=450)  # Дата
    author = models.ForeignKey(  # Автор поста, которого выбираем в административной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    body = models.TextField()  # Поле нашего поста

    def __str__(self):  # Метод
        return self.title
