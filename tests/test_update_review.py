import pytest 
from restaurant_reviews import RestaurantReviews, ReviewNotFoundError, InvalidRatingError

# Code avant Parametrization
# def test_update_existing_review():
#       rr = RestaurantReviews()
#       rr.add_review("Sushi Spot", "Fresh and tasty sushi.", 4)
#       update_result = rr.update_review("Sushi Spot", "Exceptional sushi and service.", 5) 
#       get_result = rr.get_review("Sushi Spot")
#       assert update_result == "Review added for Sushi Spot."
#       assert get_result == {'review_text' : "Exceptional sushi and service.", 'rating' : 5}

# def test_update_non_existing_review():
#       rr = RestaurantReviews()
#       with pytest.raises(ReviewNotFoundError) as excinfo:
#             rr.update_review("Grill House", "Best steaks in town.", 5)
#       assert str(excinfo.value) == "Review not found."

#Parametrization
@pytest.mark.parametrize("initial_restaurant, initial_text, initial_rating, update_restaurant, update_text, update_rating, expected_result", [
    # Update existing review with valid data
    ("Cafe Mocha", "Great coffee.", 4, "Cafe Mocha", "Excellent coffee.", 5, "Review added for Cafe Mocha."),
    # Update existing review with invalid rating
    ("Pizza Place", "Good pizza.", 3, "Pizza Place", "Great pizza!", 6, "Invalid rating. It must be between 1 and 5."),
    # Update non-existing review
    ("Sushi Spot", "Great sushi.", 4, "Sushi Express", "Fresh sushi.", 4, "Review not found.")
])
def test_update_review_parametrized(initial_restaurant, initial_text, initial_rating, update_restaurant, update_text, update_rating, expected_result):
    rr = RestaurantReviews()
    rr.add_review(initial_restaurant, initial_text, initial_rating)

    if update_rating < 1 or update_rating > 5:
        with pytest.raises(InvalidRatingError) as excinfo:
            rr.update_review(update_restaurant, update_text, update_rating)
        assert str(excinfo.value) == expected_result
