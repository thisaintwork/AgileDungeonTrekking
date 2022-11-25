from django.contrib import admin
from .models import Category, AdtCharacter
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(AdtCharacter)
class AdtCharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'character_class', 'race', 'level', 'gender', 'experience_points']
    list_filter = ['character_class', 'race', 'level']
    list_editable = ['gender', 'level', 'experience_points']
    prepopulated_fields = {'slug': ('name',)}