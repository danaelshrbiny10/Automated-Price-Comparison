from django.contrib import admin
from souq.models import Souq
from .models import category

admin.site.register(Souq)
admin.site.register(category)
