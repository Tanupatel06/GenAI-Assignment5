def apply_discount(price,percent):
    return price - (price * percent / 100)

def flat_discount(price):
    return price - 50