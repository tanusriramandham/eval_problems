""" 2)Problem Statement: Write a Python program that takes a JSON string representing an inventory of items and evaluates a conditional expression.
 The expression will check whether certain items' quantities are above a threshold and calculate the result accordingly.

Example Input:

json

{
  "item1": 50,
  "item2": 30,
  "item3": 100
}
Expression: "item1 if item1 > 40 else item2"

Output:
50
"""
import json

def evaluate_inventory_condition(json_input, expression):
    try:
        if isinstance(json_input, str):
            inventory = json.loads(json_input) 
        elif isinstance(json_input, dict):
            inventory = json_input 
        else:
            raise ValueError("Input must be a JSON string or a dictionary.")
        result = eval(expression, {}, inventory)
        return result
    except Exception as e:
        return f"Error: {e}"

json_input1 ='''{"item1": 50,"item2": 30,"item3": 100}''' #given as a string but also parsed as a dict due to json.loads
expression = "item1 if item1 > 40 else item2"
json_input2 ={"item1": 30,"item2": 40,"item3": 100}   #given a s a dict so taking directly as inventory=json_input
output1 = evaluate_inventory_condition(json_input1, expression)
print(output1)
output2 = evaluate_inventory_condition(json_input2, expression)
print(output2)