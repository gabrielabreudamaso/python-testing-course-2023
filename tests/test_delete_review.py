import pytest 

from restaurant_reviews import RestaurantReviews, ReviewNotFoundError

# Code avant Parametrization
# def test_delete_existing_review():
#     rr = RestaurantReviews()
#     rr.add_review("Pizza Place", "Great variety of pizzas.", 4)
#     get_result = rr.get_review("Pizza Place")
#     delete_result = rr.delete_review("Pizza Place")
#     assert delete_result == "Review deleted for Pizza Place."
#     with pytest.raises(ReviewNotFoundError):
#         rr.get_review("Pizza Place")

# def test_delete_non_existent_review():
#     rr = RestaurantReviews()
#     with pytest.raises(ReviewNotFoundError) as excinfo:
#         rr.delete_review("Unknown Diner")
#     assert str(excinfo.value) == "Review not found to delete."

#Parametrization
@pytest.mark.parametrize("restaurant, expected_result", [
    ("Cafe Mocha", "Review deleted for Cafe Mocha."),  # Existing review
    ("Unknown Diner", "Review not found to delete.")   # Non-existing review
])
def test_delete_review_parametrized(restaurant, expected_result):
    rr = RestaurantReviews()
    rr.add_review("Cafe Mocha", "Great coffee.", 4)
    if restaurant == "Cafe Mocha":
        assert rr.delete_review(restaurant) == expected_result
    else:
        with pytest.raises(ReviewNotFoundError) as excinfo:
            rr.delete_review(restaurant)
        assert str(excinfo.value) == expected_result

