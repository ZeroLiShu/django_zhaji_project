from django.contrib import admin

# Register your models here.
from zhaji.models import Page, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Page)
admin.site.register(Category, CategoryAdmin)
