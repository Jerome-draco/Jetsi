from django.contrib import admin
from .models import Response

# Register your models here.
@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('answer', 'created_at') # Shows columns in the dashboard