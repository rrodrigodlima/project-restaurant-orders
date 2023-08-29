from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.read_csv()

    def read_csv(self):
        dish_set = set()
        dish_dict = {}
        with open(self.source_path, 'r') as csv_file:
            content = csv.DictReader(csv_file)
            for row in content:
                if row['dish'] not in dish_set:
                    dish_set.add(row['dish'])
                    dish_dict[row['dish']] = Dish(
                        row['dish'], float(row['price'])
                    )
                ingredient = Ingredient(row['ingredient'])
                dish_dict[row['dish']].add_ingredient_dependency(
                    ingredient, int(row['recipe_amount'])
                )
        return list(dish_dict.values())
