import pytest
import unittest.mock as mock

from src.util.dao import DAO
from src.controllers.recipecontroller import RecipeController
SUFFICIENT_RECIPES = {
        "Banana Bread": 0.5,
        "Pancake": 1
}

INSUFFICIENT_RECIPES = {
    "Oatmeal" : 0.05,
    "Smoothie": 0.01
}

@pytest.fixture
def sut(readiness: float):
    sut = RecipeController(DAO)
    sut.get_readiness_of_recipes = mock.MagicMock(return_value = readiness)
    return sut

@pytest.mark.unit
@pytest.mark.parametrize('readiness, diet, optimal, expected',[(INSUFFICIENT_RECIPES, "normal", False, None)])
def test_no_recipe_found(sut, diet, optimal, expected):
    res = sut.get_recipe(diet, optimal)
    assert res == expected

@pytest.mark.unit
@pytest.mark.parametrize('readiness, diet, optimal, expected',
    [(SUFFICIENT_RECIPES, "", True, "Pancake"),
    (SUFFICIENT_RECIPES, "", False, "Pancake"),
    (SUFFICIENT_RECIPES, "vegetarian", True, "Pancake"),
    (SUFFICIENT_RECIPES, "vegetarian", False, "Pancake")
])
def test_recipe_found(sut, diet, optimal, expected):
    res = sut.get_recipe(diet, optimal)
    assert res == expected
