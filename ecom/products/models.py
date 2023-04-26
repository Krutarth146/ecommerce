from django.db import models
from user.models import User
from django_countries.fields import CountryField


class Category(models.Model):
    name = models.CharField(max_length=30)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    updated_at = models.DateTimeField(auto_now=True)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.title
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)
    
import datetime
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, blank=True, default='')
    mobile = models.CharField(max_length=12,blank=True, default='')
    date = models.DateField(default=datetime.datetime.today())
    


# from django.db import models
# from user.models import User
# from django_countries.fields import CountryField

# # Create your models here.

# LABEL_CHOICES = (
#     ('P', 'primary'),
#     ('S', 'secondary'),
#     ('D', 'danger')
# )

# ADDRESS_CHOICES = (
#     ('B', 'Billing'),
#     ('S', 'Shipping')
# )


# class OrderItem(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     item = models.ForeignKey(Item, on_delete = models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} of {self.item.title}"
    

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     ref_code = models.CharField(max_length=20, blank=True, null=True)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date =  models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#     shipping_address = models.ForeignKey(
#         'Address', related_name='shipping_address', on_delete = models.SET_NULL, blank=True, null=True
#     )
#     billing_address = models.ForeignKey(
#         'Address', related_name='billing_address', on_delete = models.SET_NULL, blank=True, null=True
#     )
#     # payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
#     coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)

#     being_delivered = models.BooleanField(default=False)
#     received = models.BooleanField(default=False)
#     refund_requested = models.BooleanField(default=False)
#     refund_granted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username
    

# class Address(models.Model):
#     user = models.ForeignKey(User,
#                              on_delete=models.CASCADE)
#     street_address = models.CharField(max_length=100)
#     apartment_address = models.CharField(max_length=100)
#     country = CountryField(multiple=False)
#     # from django_countries.fields import CountryField
#     zip = models.CharField(max_length=100)
#     address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
#     default = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

#     class Meta:
#         verbose_name_plural = 'Addresses'


# class Coupon(models.Model):
#     code = models.CharField(max_length=15)
#     amount = models.FloatField()

#     def __str__(self):
#         return self.code


# class Refund(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     reason = models.TextField()
#     accepted = models.BooleanField(default=False)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.pk}"
    

# user Profile Creation