from django.contrib import admin
from .models import company,client_data,services,Locations


admin.site.register(company)
admin.site.register(client_data)
admin.site.register(services)
admin.site.register(Locations)