from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    ingredient_name1 = 'presunto'
    ingredient_name2 = 'presunto'
    ingredient_name3 = 'salmão'
    valid_price = 5.00
    valid_dish = Dish(ingredient_name1, valid_price)
    valid_dish2 = Dish(ingredient_name2, valid_price)
    valid_dish3 = Dish(ingredient_name3, valid_price)
    ingredient = Ingredient(ingredient_name1)
    amount = 2
    expected_restrictions = {
            Restriction.ANIMAL_MEAT,
            Restriction.ANIMAL_DERIVED,
        }

    assert valid_dish.name == 'presunto'
    assert repr(valid_dish) == "Dish('presunto', R$5.00)"
    with pytest.raises(TypeError):
        Dish('presunto', '5')
    with pytest.raises(ValueError):
        Dish('presunto', -5.00)
    assert Dish.__eq__(valid_dish, valid_dish2) is True
    assert Dish.__eq__(valid_dish, valid_dish3) is False
    assert hash(valid_dish) == hash(valid_dish2)
    assert hash(valid_dish) != hash(valid_dish3)

    valid_dish.add_ingredient_dependency(ingredient, amount)
    assert ingredient in valid_dish.get_ingredients()
    assert valid_dish.get_restrictions() == expected_restrictions
