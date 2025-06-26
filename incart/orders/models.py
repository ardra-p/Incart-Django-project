from django.db import models
from customers.models import Customer
from products.models import Product
# Create your models here.

class Order(models.Model):
    LIVE =1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFORMED ='ORDER_CONFORMED '
    ORDER_PROCESSED='ORDER_PROCESSED'
    ORDER_REJECTED ='ORDER_REJECTED'
    ORDER_DELIVERED = 'ORDER_DELIVERED'
    STATUS_CHOICE=((ORDER_PROCESSED,'ORDER_PROCESSED'),
                   (ORDER_DELIVERED,'ORDER_DELIVERED'),
                   (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status=models.CharField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,related_name='orders') #onetomany relation
    detele_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:

        return "order-{}-{}".format(self.id,self.owner.user.username)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    size =models.CharField(max_length=20,null=True,blank=True)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='added_items')


