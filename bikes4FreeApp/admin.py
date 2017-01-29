from django.contrib import admin

from .models import Combo
admin.site.register(Combo)


from rest_framework.authtoken.admin import TokenAdmin
TokenAdmin.raw_id_fields = ('user',)