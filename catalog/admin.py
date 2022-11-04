from django.contrib import admin

from .models import Cities, Client, LogModel, Person, Product, Providers


class LodAdmin(admin.ModelAdmin):
    list_display = ['path', 'method', 'custom_attr_get', 'custom_attr_post', 'timestamp']
    list_filter = ['timestamp', 'method']
    search_fields = ['path']
    date_hierarchy = 'timestamp'

    @admin.display(boolean=True)
    def custom_attr_get(self, obj):
        return True if obj.request_get else False
    custom_attr_get.short_description = 'value_get'

    @admin.display(boolean=True)
    def custom_attr_post(self, obj):
        return True if obj.request_post else False
    custom_attr_post.short_description = 'value_post'


admin.site.register(Cities)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Providers)
admin.site.register(Person)
admin.site.register(LogModel, LodAdmin)
