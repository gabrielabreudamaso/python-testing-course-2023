import pytest
# n'oubliez pas le __ini__.py dans le dossier afin d'importer la Classe
from restaurant_reviews import RestaurantReviews, InvalidRatingError

# Code avant Parametrization
# def test_add_valid_review():
#     rr = RestaurantReviews()
#     result = rr.add_review("Cafe Mocha", "Great coffee and pastries.", 4)
#     assert result == "Review added for Cafe Mocha."

# #Testez l'ajout d'un avis avec une note invalide (par exemple, note > 5).
# def test_add_invalid_rating():
#     rr = RestaurantReviews()
#     with pytest.raises(InvalidRatingError) as excinfo:
#         rr.add_review("Cafe Mocha", "Good ambiance.", 6)
#     assert str(excinfo.value) == "Rating must be between 1 and 5."

#Parametrization
@pytest.mark.parametrize("restaurant, review_text, rating, expected_result", [
    ("Cafe Mocha", "Great coffee.", 4, "Review added for Cafe Mocha."),
    ("Burger Bistro", "Amazing burgers.", 5, "Review added for Burger Joint."),
    ("Pizza Place", "Delicious pizza.", 1, "Review added for Pizza Place."),
    ("Sushi Spot", "Fresh sushi.", 0, "It must be between 1 and 5."),  # Invalid rating
    ("Taco Stand", "Tasty tacos.", 6, "It must be between 1 and 5.")   # Invalid rating
])
def test_add_review_parametrized(restaurant, review_text, rating, expected_result):
    rr = RestaurantReviews()
    if rating < 1 or rating > 5:
        with pytest.raises(InvalidRatingError) as excinfo:
            rr.add_review(restaurant, review_text, rating)
        assert str(excinfo.value) == expected_result
    else:
        assert rr.add_review(restaurant, review_text, rating) == expected_result