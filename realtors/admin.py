from django.contrib import admin
from . models import Realtor
class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','hire_date']
    list_display_links = ['id','name','email']
    list_editable = ['phone']
    search_fields = ['name','email','phone']
    list_per_page = 25
    list_filter = ('hire_date',)
admin.site.register(Realtor,RealtorAdmin)
