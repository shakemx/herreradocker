from django.contrib import admin
from django import forms
from entities.models import Type, Category, Product
from agents.models import Agent


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('name', 'is_active')
    search_fields = ('name', 'is_active')
    exclude = ('description',)

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Seguro'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Seguro'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'is_active')
    list_filter = ('name', 'type', 'is_active')
    search_fields = ('name', 'type', 'is_active')
    exclude = ('description',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type':
            kwargs['queryset'] = Type.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Seguro'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Seguro'



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_type','is_active', 'fav')
    list_filter = ('name', 'category', 'is_active', 'fav')
    search_fields = ('name', 'category', 'is_active',  'fav')

    def get_type(self, obj):
        return obj.category.type.name
    get_type.short_description='Type'
    get_type.admin_order_field='category__type__name'


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            kwargs['queryset'] = Category.objects.filter(is_active=True)
            return CategoryChoiceField(queryset=Category.objects.filter(is_active=True))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Seguro'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Seguro'

class CategoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.type.name} - {obj.name}'
    
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name','is_active')

admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Agent, AgentAdmin)
