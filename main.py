from collections import defaultdict

def most_varied(recipes):
    # Write your solution here!
    unique_ing_dict= defaultdict(set)

    for item in recipes: # O(n)
        unique_ing_dict[item[1]].update(set(item[2]))
    
    
    sorted_recipes = sorted(unique_ing_dict.items(), key=lambda item: len(item[1]), reverse=True) # o(mlog(m)) m:max ingrid counts

    top_two = sorted_recipes[:2]
    output = []

    for item in top_two: # item is a tuple(chef, unique ingrd) 
        output_item = (item[0],sorted(list(item[1]))) 
        output.append(output_item)
    
    return output


recipes_1 = [
    ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
    ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
    ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
    ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
print(most_varied(recipes_1))

assert most_varied(recipes_1) == [
    ("Xinting", ["Beef", "Carrot", "Chicken Stock", "Onion", "Peas", "Tomato"]), 
    ("Amy", ["Cheese", "Chicken Cream", "Pepper", "Tater tots"])
]

recipes_2 = [
    ("Latkes", "Hallie", ("Potato", "Oil")),
    ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]
assert most_varied(recipes_2) == [
    ("Sam", ["Beef", "Cheese", "Tortilla"]),
    ("Hallie", ["Oil", "Potato"])
]

print("All test cases passed!")
print("Finished early? Discuss time & space complexity.")