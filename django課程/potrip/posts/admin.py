from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.
from .models import Location,Post

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class PostAdmin(admin.ModelAdmin):
    list_display = ('subject','content','author','location')
    fields = ('subject','content','author','location')

admin.site.register(Location,LocationAdmin)
admin.site.register(Post,PostAdmin)