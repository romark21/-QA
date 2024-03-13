def calculate_discount(points):
    discount = None

    if 0 < points <= 100:
        discount = 1

    elif 100 < points <= 200:
        discount = 3

    elif 200 < points <= 500:
        discount = 5

    elif 500 < points:
        discount = 10

    print(f'Calculated discount is {discount}%')
    return discount



