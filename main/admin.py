from django.contrib import admin
from .models import Category, Product, Slider

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ["name"] }
    search_fields = ["name"]
    search_help_text = ["You can search with category name"]
    
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "discount", "available"]
    list_filter = ["available", "created_at", "updated_at", "category"]    
    list_display_links = ["name"]    
    list_editable = ["available", "price", "discount"]
    prepopulated_fields = {"slug" : ["name"]} 
    search_fields = ["name"]
    search_help_text = ["You can search with product name"]
    
    
@admin.register(Slider)
class SliderAmin(admin.ModelAdmin):
    list_display = ["name", "descr", "created_at", "updated_at"]
    list_filter = ["name", "created_at"]
    list_display_links = ["name"]    
