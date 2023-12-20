import pytest

from restaurant_reviews import RestaurantReviews, ReviewNotFoundError

# Code avant Parametrization
# def test_get_existing_review():
#     rr = RestaurantReviews()
#     rr.add_review("Pasta Palace", "Delicious pasta dishes.", 5)
#     result = rr.get_review("Pasta Palace")
#     assert result == {'review_text': "Delicious pasta dishes.", 'rating' :5}

# def test_get_non_existing_review():
#     rr = RestaurantReviews()
#     with pytest.raises(ReviewNotFoundError) as excinfo:
#         rr.get_review("Burger Bistro")
#     assert str(excinfo.value) == "Review not found."

#Parametrization
@pytest.mark.parametrize("restaurant, expected_output", [
    ("Cafe Mocha", {'review_text': "Great coffee.", 'rating': 4}),  # Existing review
    ("Burger Joint", {'review_text': "Amazing burgers.", 'rating': 5}),  # Existing review
    ("Unknown Diner", "Review not found.")  # Non-existing review
])
def test_get_review_parametrized(restaurant, expected_output):
    rr = RestaurantReviews()
    rr.add_review("Cafe Mocha", "Great coffee.", 4)
    rr.add_review("Burger Bistro", "Amazing burgers.", 5)
    if restaurant == "Unknown Diner":
        with pytest.raises(ReviewNotFoundError) as excinfo:
            rr.get_review(restaurant)
        assert str(excinfo.value) == expected_output
    else:
        assert rr.get_review(restaurant) == expected_output