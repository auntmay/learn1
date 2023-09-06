def discounted(price, discount, max_discount=30, phone_name = ''):
    
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    
    if not phone_name or 'iphone' in phone_name.lower():
        return price
    elif discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
    

new_price = discounted(100000, 10, phone_name = 'IPhone 12')
print(new_price)

new_price = discounted(40000, 20, phone_name = 'Xmi')
print(new_price)

new_price = discounted(5000, 20)
print(new_price)