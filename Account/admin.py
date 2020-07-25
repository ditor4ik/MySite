from django.contrib import admin
from .models import User

@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'NickName', 'Password','email','vip_status','Created',]
    search_fields = ['NickName', 'user_id']
    list_filter = ['vip_status', 'Created']