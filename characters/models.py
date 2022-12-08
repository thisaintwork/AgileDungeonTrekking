import os.path
import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from .generate import GenerateCharacter


class Category(models.Model):
    """ Class for filtering a player's list of characters """
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('characters_by_category', args=[self.slug])


class AdtCharacter(models.Model):

    category = models.ForeignKey(Category,
                                 related_name='character_class',
                                 on_delete=models.CASCADE,
                                 default=0)
    pid = models.UUIDField(default=uuid.uuid4,
                           editable=False)
    slug = models.SlugField(max_length=200, default='', db_index=True)
    name = models.CharField(max_length=150, default='no name', db_index=True)
    age = models.FloatField(default=0)
    gender = models.CharField(max_length=1, default='O')
    charisma = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    experience_points = models.PositiveIntegerField(default=0)
    character_class = models.CharField(max_length=100, blank=True, db_index=True)
    race = models.CharField(max_length=50, default='human')
    alignment = models.CharField(max_length=100, default='neutral')
    platinum = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    copper = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    created_by = models.CharField(max_length=100, default='unknown')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"Name: {self.name}, Class: {self.character_class}, Race: {self.race}, Level: {self.level}"

    def get_absolute_url(self):
        return reverse('character_detail', args=[self.id])

    def generate_attributes(**kwargs):
        # call the dnd-character object to generate attributes
        gen = GenerateCharacter()
        character = gen.CreateCharacter(kwargs)
        return character

    @property
    def image_name(self):

        return os.path.basename(self.image.path) if self.image else ''
