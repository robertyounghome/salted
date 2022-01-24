from django.contrib import admin
from my_passwords.models import Category, Account

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)