from django.contrib import admin
from  .models import Category, Product

# Register your models here.
from.models import Student

admin.site.register(Student)

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
 list_display = ('title', 'category', 'price')
 list_filter = ('category',)
 search_fields = ('title',)


# Customize the admin panel

admin.site.site_header = "MyProject Admin" #Top-left header
admin.site.site_title = "MyProject Admin Portal" # Browser tab title
admin.site.index_title = "Welcome to MyProject Admin Dashboard" # Index page
