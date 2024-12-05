from django.db import models
from django.urls import reverse

from base.models import BaseModel
from autoslug import AutoSlugField


class Agent(BaseModel):
    USER = 'USER'
    COMPANY = 'COMPANY'
    CHOICE_TYPE =[
        (USER, 'Usuario'),
        (COMPANY, 'Empresa'),
    ]
    name = models.CharField('Nombre', max_length=50, blank=False, null=False)
    mail = models.EmailField('Correo')
    phone = models.CharField('Teléfono', max_length=15, blank=True,)
    mobile = models.CharField('Celular', max_length=15, blank=False, null=False)
    whatsapp = models.CharField('Whatsapp Business', max_length=15, blank=False, null=False)
    web = models.URLField('Sitio Web',blank=True,)
    schedule = models.CharField('Horario', max_length=100, blank=True,)
    type = models.CharField('Tipo', max_length=10, choices=CHOICE_TYPE, default=USER, blank=False)
    name = models.CharField('Nombre', max_length=150, blank=False, null=False)
    photo = models.ImageField('Foto de Perfil', blank=True)
    cover = models.ImageField('Foto de Portada', blank=True)
    role = models.CharField('Puesto/Rol', max_length=50, blank=True)
    bio = models.TextField('Biografía', max_length=500, blank=True)
    slug_agent = AutoSlugField(populate_from='name', unique=True, always_update=False)


    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('agent', kwargs={'slug_agent': self.slug_agent})