from django.contrib import admin
from form.models import Information

class admin_panals(admin.ModelAdmin):
    list_display=('id','name','designation','qualification','experiance','expetarea','email','mob','image','pdf')

admin.site.register(Information,admin_panals)

# Register your models here.
