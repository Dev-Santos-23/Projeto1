from django.contrib import admin

from .models import Category, Recipe

class CategoryAdmim(admin.ModelAdmin):
    ...
@admin.register(Recipe)
class RecipeAamin(admin.ModelAdmin):
     ... 
      
admin.site.register(Category, CategoryAdmim)
    