from db_api.models import Menu, Submenu, Dish
from db_api.database import BASE, engine_test


BASE.metadata.create_all(engine_test)