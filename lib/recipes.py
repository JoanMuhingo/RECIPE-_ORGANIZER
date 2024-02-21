from model import Recipe, session

def create_recipe(name, description, instructions, cook_time, user_id, category_id)
new_recipe = Recipe(
    name=name,
    description=description,
    instructions=instructions,
    cook_time=cook_time,
    user_id=user_id,
    Category_id=category_id
)
session.add(new_recipe)
session.commit()
return new_recipe