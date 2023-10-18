from django.db import models
from django.contrib import admin
class players(models.Model):
    player_name=models.CharField(max_length=20)
    players_age=models.CharField(max_length=100)
    native_place=models.CharField(max_length=30)
    salary=models.IntegerField()
    no_of_winnings=models.IntegerField()

class playersAdmin(admin.ModelAdmin):
    list_display=('player_name','players_age','native_place','salary','no_of_winnings')


# Create your models here.
