"""
Create a list called menu,
Create a dictionary called stock
(This should contain the stock value for each item on the menu)
Create another dictionary called price
(This should contain the prices for each item)
Calculate the total stock worth in the cafe
(use item_value = (stock[items] * price[items]))
Finally print the result

"""
import json
# Create a list with the items available to order
menu =['coffee', 'tea', 'biscuit', 'vegan cake']

# Create a dictionary containing the stocks
stock = {"coffee": 125,
          "tea":  102,
          "biscuit": 500,
          "vegan cake": 15,
            }


# Create a dictionary containing the prices for each item
price = {"coffee":  2.69,
          "tea":  1.50,
          "biscuit":  1.20,
          "vegan cake":  3.25,
          }

# to print out the stock value for each of the items 
for x in stock.values():
  print(x)

print("*" * 140) # to separate our values, result is easier to read

# to print out the price for each of the items 
for x in price.values():
  print(x)

print("*" * 140) # to separate our values, result is easier to read


# print the values in the price dictionary for each item individually
for x, y in price.items():
  print(y)

print("*" * 140) # to separate our values, result is easier to read


# print out the stock value / item
for (i, j) in zip(stock, price): 
    stock_value = (stock[i] * price[j])  
    print(stock_value)
