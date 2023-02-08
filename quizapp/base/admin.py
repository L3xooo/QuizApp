from django.contrib import admin
from .models import Player,Question,Quiz
# Register your models here.

admin.site.register(Player),
admin.site.register(Question),
admin.site.register(Quiz)