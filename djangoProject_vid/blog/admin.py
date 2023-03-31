from django.contrib import admin
from .models import Post
from .models import BirdPost
from .models import MammalsPost
from .models import FishPost

admin.site.register(Post)  # Регистрация модели нашего поста
admin.site.register(BirdPost)
admin.site.register(MammalsPost)
admin.site.register(FishPost)