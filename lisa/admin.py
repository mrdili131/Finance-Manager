from django.contrib import admin
from .models import Finance, Category

admin.site.register([Finance, Category])