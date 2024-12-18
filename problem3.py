"""3) You are given a list of dictionaries where each dictionary represents a product with its name and price. 
Write a program that:

Creates a lambda function to apply a discount of 10% to the price of each product.
Use eval() to evaluate an expression that applies this lambda function to the product list.
Output the list of products with the updated prices after applying the discount.
Example Input:

json

[
    {"name": "apple", "price": 30},
    {"name": "banana", "price": 20},
    {"name": "cherry", "price": 50}
]
Expression: "list(map(lambda x: {'name': x['name'], 'price': round(x['price'] * 0.9, 2)}, products))"

Expected Output:

json
[
    {"name": "apple", "price": 27.0},
    {"name": "banana", "price": 18.0},
    {"name": "cherry", "price": 45.0}
]
"""
import json 
def apply_discount(product_list,expression):
    try:
        updated_products=eval(expression,{},{"products":product_list})
        return updated_products
    except Exception as e:
        return (f"Error: {e}")
    
product_list=[
    {"name": "apple", "price": 30},
    {"name": "banana", "price": 20},
    {"name": "cherry", "price": 50}
]

expression="list(map(lambda x: {'name': x['name'], 'price': round(x['price'] * 0.9, 2)}, products))"
updated_products=apply_discount(product_list,expression)
print(json.dumps(updated_products,indent=3))