from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(data,cart):
    print(data.product_id)

    keys=cart.keys()
    print(cart)
    for ine in keys:
        if int(ine)==int(data.product_id):
            return True
   
    # print(cart)

    return False

@register.filter(name='cart_quantity')
def cart_quantity(data , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == data.product_id:
            return cart.get(id)
    return 0;



@register.filter(name='price_total')
def price_total(product  , cart):
    return product.price * cart_quantity(product , cart)


@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0 ;
    for p in products:
        sum += price_total(p , cart)

    return sum