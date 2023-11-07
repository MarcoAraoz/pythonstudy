#Black Friday Discounts

price = int(input('Enter the article cost: ' ).strip())

# The code is calculating the discounted price of an item based on its original price (`precio`).

# The code it applies a discount of 30% by multiplying the price by 0.7.
if price >= 300:
    price *= 0.7
#It applies a discount of 20% by multiplying the price by 0.8.
elif price >=200:
    price*= 0.8
# If the original price of the item is between 100 and
# 199 (inclusive), the price will be reduced by 10%.
elif price >= 100:
    price *= 0.9
# If the original price of the item is less than 100,
# the price will be reduced by 5%.
elif price < 100 and price >= 0:
    price *= 0.95
    
print(price)
# 500
# 350.0