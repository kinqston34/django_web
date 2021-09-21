from .models import Customer,Detail
from django.contrib import admin

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','location')
    
class DetailAdmin(admin.ModelAdmin):
    list_display = ('name','line_id','email','tel','suggest')
    

    
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Detail,DetailAdmin)
