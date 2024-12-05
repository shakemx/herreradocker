from django.urls import path, re_path
from django.conf import settings

from web.views import home, insurance, product, insurances, agent, agent_card, vcard

urlpatterns = [
    path('', home, name='home'),
    path('portafolio/<slug:slug_type>', insurance, name='insurance'),
    path('portafolio/<slug:slug_type>/<slug:slug_category>', insurances, name='insurances'),
    path('portafolio/<slug:slug_type>/<slug:slug_category>/<slug:slug_product>', product, name='product'),
    path('agentes', agent, name='agent'),
    path('agente/<slug:slug_agent>', agent_card, name='agent_card'),
    path('vcard/<slug:slug_agent>', vcard, name='vcard'),
    re_path(r'^portafolio/<slug:slug_type>\/?$', insurance, name='insurance'),
    re_path(r'^agentes\/?$', agent, name='agent'),
    re_path(r'^agente/<slug:slug_agent>\/?$', agent_card, name='agent_card'),
    re_path(r'^portafolio/<slug:slug_type>/<slug:slug_category>\/?$', insurances, name='insurances'),
    re_path(r'^portafolio/<slug:slug_type>/<slug:slug_category>/<slug:slug_product>\/?$', product, name='product'),
] 