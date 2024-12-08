from django.contrib import admin
from . models import Post, Category, Location


class PostAdmin(admin.ModelAdmin):
    ...


class CategoryAdmin(admin.ModelAdmin):
    ...


class LocationAdmin(admin.ModelAdmin):
    ...


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
