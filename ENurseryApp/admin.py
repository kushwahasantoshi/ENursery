from django.contrib import admin
from ENurseryApp.models import Product, CustomUser, Category
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('address', 'pin')}),
    )

class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','category','description','image']


admin.site.register(Category)
admin.site.register(CustomUser)
admin.site.register(Product,AdminProduct)