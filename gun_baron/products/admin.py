from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 0


class ProductAdmin(admin.ModelAdmin):
		list_display = [field.name for field in Product._meta.fields]
		inlines = [ProductImageInline]

		class Meta:
			model = Product


class CommentAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Comment._meta.fields]

	class Meta:
		model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)

admin.site.register(Category)

admin.site.register(Comment, CommentAdmin)