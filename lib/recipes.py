from models import Recipe, session

def create_recipe(name, description, instructions, cook_time, user_id, category_id):
    new_recipe = Recipe(
        name=name,
        description=description,
        instructions=instructions,
        cook_time=cook_time,
        user_id=user_id,
        category_id=category_id
    )

    session.add(new_recipe)
    session.commit()
    return new_recipe
    

def add_recipe():
    name = input("Enter recipe name: ")
    description = input("Enter recipe description: ")
    instructions = input("Enter recipe instructions: ")
    cook_time = int(input("Enter cook time (in minutes): "))
    user_id = input("Enter your name: ")
    category_id = input("Enter category name: ")
    
    if user_id is None or category_id is None:
        print("Recipe not added. User or category not found.")
        return None


    new_recipe = Recipe(
        name=name,
        description=description,
        instructions=instructions,
        cook_time=cook_time,
        user_id=user_id,
        category_id=category_id
    )

    return new_recipe

if __name__ == "__main__":
    new_recipe = add_recipe()
    print("New Recipe added:", new_recipe)
