from django.contrib import admin
from .models import juice, menucold,menuhot, special

admin.site.register(menucold)
admin.site.register(menuhot)
admin.site.register(juice)
admin.site.register(special)