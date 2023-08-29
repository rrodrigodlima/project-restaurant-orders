from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    flour1 = Ingredient('farinha')
    flour2 = Ingredient('farinha')
    rice1 = Ingredient('arroz')
    rice2 = Ingredient('arroz')
    rice2.restrictions.add(Restriction.GLUTEN)

    assert flour1.name == 'farinha'
    assert flour1.restrictions == {Restriction.GLUTEN}
    assert repr(flour1) == "Ingredient('farinha')"

    assert rice1.restrictions == set()

    assert hash(flour1) == hash(flour2)
    assert hash(flour1) != hash(rice1)

    assert flour1 == flour2
    assert rice1 == rice2

    assert not (flour1 == rice1)
    assert not (flour2 == rice2)
