import os
import json
import random

"""
Question 1: Which item had the most sales?
Question 2: How much revenue was made on ale?
Question 3: What was the least popular item?
"""

items = ["sword", "pickaxe", "health potion", "bow", "ale"]
units_sold = [4, 2, 10, 1, 40]
prices = [10.0, 9.0, 2.0, 15, 1.50]

revenue = [units_sold[x] * prices[x] for x in range(0, len(units_sold))]

response = {
    "question 1": random.choices(items, weights=units_sold)[0],
    "question 2": random.choices(revenue, weights=units_sold)[0],
    "question 3": random.choices(items, weights=units_sold)[0]
}

if not os.path.exists("output"):
    os.mkdir("output")

json_object = json.dumps(response)
with open("output/answers.json", "w") as file:
    file.write(json_object)

file_min = random.choices([0,1,2,3], weights=[50,20,10,5])[0]

for x in range(file_min):
    extension = random.choices(["txt", "json", "png", "jpg", "gif"], weights=[50,40,10,10,10])[0]

    with open(os.path.join(f"output/file_{x}.{extension}"), "w") as file:
        file.write(json_object)

print("I have completed")
