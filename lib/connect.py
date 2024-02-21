from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Recipe, Ingredient, RecipeIngredient

engine = create_engine("sqlite:///recipe.db")

Base.metadata.create_all(engine)

print("Database tables created.")