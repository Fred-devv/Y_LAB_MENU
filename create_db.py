from db_api.models import Menu, Submenu, Dish
from db_api.database import BASE, engine


BASE.metadata.create_all(engine)