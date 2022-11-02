from django.contrib import admin

from .models import Cities, Client, Person, Product, Providers


admin.site.register(Cities)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Providers)
admin.site.register(Person)
