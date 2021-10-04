from django.contrib import admin
from django.db import models
from .models import new,Breaking

# Register your models here.
@admin.register(new)
class newsAdmin(admin.ModelAdmin):
    list_display = ['news_name','news_category','news_subcategory','news_author']


@admin.register(Breaking)
class breakingAdmin(admin.ModelAdmin):
    list_display = ['breaking']