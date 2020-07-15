from django.contrib import admin
from .models import User

@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['NickName', 'Password','email','vip_status','Created',]
    list_filter = ['vip_status', 'Created']