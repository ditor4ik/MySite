from django.contrib import admin
from .models import BookModel
@admin.register(BookModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'user_id', 'Header','Rating']
    search_fields = ['book_id', 'user_id']
# Register your models here.
