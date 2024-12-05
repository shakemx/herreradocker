from django.shortcuts import render, redirect, get_object_or_404

from entities.models import Type, Category, Product 
from agents.models import Agent
import vobject
from django.http import HttpResponse


def home(request):
    if request.method == 'GET':
        types = Type.objects.filter(is_active=True).order_by('name')
        categories = Category.objects.prefetch_related('type').filter(is_active=True).order_by('type__name')
        products = Product.objects.prefetch_related('category').filter(is_active=True).order_by('category__type__name')
        favs = Product.objects.filter(fav=True, is_active=True).order_by('name')
        favs = favs[:5]
        agents = Agent.objects.filter(is_active=True).order_by('name')
        context ={'types' : types,
                  'categories' : categories,
                  'products' : products,
                    'favs' : favs,
                    'agents' : agents,
        }
        return render(request, 'home.html', context=context)
    return redirect('home')

def insurance(request, slug_type):
    if request.method == 'GET':
        agents = Agent.objects.filter(is_active=True).order_by('name')
        products = Product.objects.prefetch_related('category').filter(is_active=True).order_by('category__type__name')
        insurance = get_object_or_404(Type, slug_type=slug_type, is_active=True)
        categoriesInsurance = Category.objects.prefetch_related('type').filter(type=insurance, is_active=True).order_by('name')
        productsInsurance = Product.objects.select_related('category').filter(category__type=insurance, is_active=True).order_by('name')
        context ={'insurance' : insurance,
                   'products' : products,
                    'agents' : agents,
                  'categoriesInsurance' : categoriesInsurance,
                  'productsInsurance' : productsInsurance,}
        return render(request, 'insurance.html', context=context)
    return redirect('home')

def insurances(request, slug_type, slug_category):
    if request.method == 'GET':
        agents = Agent.objects.filter(is_active=True).order_by('name')
        products = Product.objects.prefetch_related('category').filter(is_active=True).order_by('category__type__name')
        insurance = get_object_or_404(Type, slug_type=slug_type, is_active=True)
        categoriesInsurance = Category.objects.prefetch_related('type').filter(type=insurance, is_active=True).order_by('name')
        productsInsurance = Product.objects.select_related('category').filter(category__type=insurance , category__slug_category=slug_category,is_active=True).order_by('name')
        context ={'insurance' : insurance,
                  'products' : products,
                    'agents' : agents,
                  'categoriesInsurance' : categoriesInsurance,
                  'productsInsurance' : productsInsurance,}
        return render(request, 'insurance.html', context=context)
    return redirect('home')

def product(request, slug_type, slug_category, slug_product):
    if request.method == 'GET':
        agents = Agent.objects.filter(is_active=True).order_by('name')
        products = Product.objects.prefetch_related('category').filter(is_active=True).order_by('category__type__name')
        product = get_object_or_404(Product, slug_product=slug_product, category__type__slug_type=slug_type, category__slug_category=slug_category, is_active=True)
        context ={'product' : product,
                     'agents' : agents,
                   'products' : products,}
        return render(request, 'product.html', context=context)
    return redirect('home')

def agent(request):
    if request.method == 'GET':
        agents = Agent.objects.filter(is_active=True).order_by('name')
        products = Product.objects.prefetch_related('category').filter(is_active=True).order_by('category__type__name')
        context ={'agents' : agents,
                   'products' : products}
        return render(request, 'agents.html', context=context)
    return redirect('home')

def agent_card(request, slug_agent):
    if request.method == 'GET':
        list_agent = get_object_or_404(Agent, slug_agent=slug_agent, is_active=True)
        products = Product.objects.prefetch_related('category').filter(is_active=True).order_by('category__type__name')
        context ={'list_agent' : list_agent,
                   'products' : products}
        return render(request, 'agent_card.html', context=context)
    return redirect('home')

def vcard(request, slug_agent):
    user = get_object_or_404(Agent, slug_agent=slug_agent)
    vcard_data = vobject.vCard()
    vcard_data.add('n')
    vcard_data.n.value = vobject.vcard.Name(family=user.name, given='')
    vcard_data.add('fn')
    vcard_data.fn.value = user.name
    vcard_data.add('email')
    vcard_data.email.value = user.mail
    vcard_data.email.type_param = 'Correo Electrónico'
    vcard_data.add('tel')
    vcard_data.tel.value = user.mobile
    vcard_data.tel.type_param = 'Celular'
    vcard_data.add('tel')
    vcard_data.tel.value = user.phone
    vcard_data.tel.type_param = 'Teléfono'
    vcard_data.add('url')
    vcard_data.url.value = user.web
    vcard_data.url.type_param = 'Sitio Web'
    response = HttpResponse(vcard_data.serialize(), content_type='text/x-vCard')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format('{}.vcf'.format(user.name))
    return response

