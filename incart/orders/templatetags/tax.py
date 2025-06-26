from django import template

register = template.Library()

@register.simple_tag(name='tax')
def tax(cart):
    total=0
    for item in cart.added_items.all():
        total+=item.quantity*item.product.price
        
    taxamount=(0.65/100)*total

    return round(taxamount,2)