from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from web.views import home, insurance, product, insurances
urlpatterns = [
    path('', home, name='home'),
    path('portafolio/<slug:slug_type>', insurance, name='insurance'),
    path('portafolio/<slug:slug_type>/<slug:slug_category>', insurances, name='insurances'),
    path('portafolio/<slug:slug_type>/<slug:slug_category>/<slug:slug_product>', product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)