from django.urls import path, re_path
from django.conf import settings

from web.views import home, insurance, product, insurances
urlpatterns = [
    path('', home, name='home'),
    path('portafolio/<slug:slug_type>', insurance, name='insurance'),
    path('portafolio/<slug:slug_type>/<slug:slug_category>', insurances, name='insurances'),
    path('portafolio/<slug:slug_type>/<slug:slug_category>/<slug:slug_product>', product, name='product'),
    re_path(r'^portafolio/<slug:slug_type>\/?$', insurance, name='insurance'),
    re_path(r'^portafolio/<slug:slug_type>/<slug:slug_category>\/?$', insurances, name='insurances'),
    re_path(r'^portafolio/<slug:slug_type>/<slug:slug_category>/<slug:slug_product>\/?$', product, name='product'),
] 