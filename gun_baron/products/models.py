from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from auth_reg.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '%s' % (self.name)

    def get_product(self):
        return self.product_set.all()


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    price = models.BigIntegerField(default=1)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None, max_length=40)

    def __str__(self):
        return '%s %s' % (self.name, self.price)

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('product', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_comment(self):
        return self.comment_set.all()

    def get_image(self):
        return self.productimage_set.filter(main=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    main = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'id=%s name=%s main=%s' % (self.id, self.product, self.main)


class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, blank=True)
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    comment_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, default=None, blank=True)

    def __str__(self):
        return 'id=%s' % (self.id)
