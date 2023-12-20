# Function que j'ai envie d'implémenter
def total_with_tip(bill, percentage):
    return 120

# TDD - Test Driven Development
# 1. Pour un repas à *100€* (bill), et un tips de *20%*(percentage) : Je laisse sur la table *120€*(output/return).
def test_tip_classic():
    assert total_with_tip(100, 20) == 120

def test_tip_poor_service():
    assert total_with_tip(100, 0) == 100
