from django.contrib import admin
from .models import Category, Subcategory, Service, News

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Service)
admin.site.register(News)
