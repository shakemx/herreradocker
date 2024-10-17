from django.db import models
from django.urls import reverse

from base.models import BaseModel
from autoslug import AutoSlugField

    

class Type(BaseModel):
    name = models.CharField('Nombre', max_length=255)
    cover = models.ImageField('Portada', blank=True, default=None, null=True)
    lead = models.CharField('Lead', max_length=255)
    description = models.TextField('Descripción', null=True, default=None, blank=True)
    slug_type = AutoSlugField(populate_from='name', unique=True, always_update=False)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home', kwargs={'slug_type': self.slug_type})


class Category(BaseModel):
    name = models.CharField('Nombre', max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')
    cover = models.ImageField('Portada', blank=True, default=None, null=True)
    lead = models.CharField('Lead', max_length=255)
    description = models.TextField('Descripción', null=True, default=None, blank=True)
    slug_category = AutoSlugField(populate_from='name', unique=True, always_update=False)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home', kwargs={'slug_category': self.slug_category})
    
class Product(BaseModel):
    name = models.CharField('Nombre', max_length=255)
    slug_product = AutoSlugField(populate_from='name', unique=True, always_update=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField('Portada', blank=True, default=None, null=True)
    image_2 = models.ImageField('Contenido', blank=True, default=None, null=True)
    video = models.URLField('Youtube URL', blank=True, default=None, null=True)
    definicion = models.TextField('Definición', null=True, default=None, blank=True)
    beneficio = models.TextField('Beneficio', null=True, default=None, blank=True)
    elegibilidad = models.TextField('Elegibilidad', null=True, default=None, blank=True)
    exepciones = models.TextField('Excepciones', null=True, default=None, blank=True)
    adicionales = models.TextField('Adicionales', null=True, default=None, blank=True)
    caracteristicas = models.TextField('Caracteristicas', null=True, default=None, blank=True)
    fav = models.BooleanField('Favorito', default=False, null=True, blank=True)
    slug_product = AutoSlugField(populate_from='name', unique=True, always_update=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home', kwargs={'slug_product': self.slug_product})

