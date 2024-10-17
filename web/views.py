from django.shortcuts import render, redirect, get_object_or_404

from entities.models import Type, Category, Product


def home(request):
    if request.method == 'GET':
        types = Type.objects.filter(is_active=True).order_by('name')
        categories = Category.objects.prefetch_related('type').filter(is_active=True).order_by('type__name')
        products = Product.objects.prefetch_related('category').filter(is_active=True).order_by('category__type__name')
        favs = Product.objects.filter(fav=True, is_active=True).order_by('name')
        favs = favs[:5]
        context ={'types' : types,
                  'categories' : categories,
                  'products' : products,
                    'favs' : favs,
        }
        return render(request, 'home.html', context=context)
    return redirect('home')

def insurance(request, slug_type):
    if request.method == 'GET':
        insurance = get_object_or_404(Type, slug_type=slug_type, is_active=True)
        categoriesInsurance = Category.objects.prefetch_related('type').filter(type=insurance, is_active=True).order_by('name')
        productsInsurance = Product.objects.select_related('category').filter(category__type=insurance, is_active=True).order_by('name')
        context ={'insurance' : insurance,
                  'categoriesInsurance' : categoriesInsurance,
                  'productsInsurance' : productsInsurance,}
        return render(request, 'insurance.html', context=context)
    return redirect('home')

def insurances(request, slug_type, slug_category):
    if request.method == 'GET':
        insurance = get_object_or_404(Type, slug_type=slug_type, is_active=True)
        categoriesInsurance = Category.objects.prefetch_related('type').filter(type=insurance, is_active=True).order_by('name')
        productsInsurance = Product.objects.select_related('category').filter(category__type=insurance , category__slug_category=slug_category,is_active=True).order_by('name')
        context ={'insurance' : insurance,
                  'categoriesInsurance' : categoriesInsurance,
                  'productsInsurance' : productsInsurance,}
        return render(request, 'insurance.html', context=context)
    return redirect('home')

def product(request, slug_type, slug_category, slug_product):
    if request.method == 'GET':
        product = get_object_or_404(Product, slug_product=slug_product, category__type__slug_type=slug_type, category__slug_category=slug_category, is_active=True)
        context ={'product' : product}
        return render(request, 'product.html', context=context)
    return redirect('home')


