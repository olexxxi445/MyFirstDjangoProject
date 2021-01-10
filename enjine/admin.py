from django.contrib import admin
from enjine.models import Req
# Register your models here

#admin.site.register(Req)

@admin.register(Req)
class ReqAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone']


