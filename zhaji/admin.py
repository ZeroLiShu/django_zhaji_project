from django.contrib import admin

# Register your models here.
from zhaji.models import Book, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Book)
admin.site.register(Category, CategoryAdmin)
