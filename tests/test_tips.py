# Function que j'ai envie d'implémenter
def total_with_tip(bill, percentage):
    total = bill + (percentage/100*bill)
    return total

# TDD - Test Driven Development
# 1. Pour un repas à *100€* (bill), et un tips de *20%*(percentage) : Je laisse sur la table *120€*(output/return).
def test_tip_classic():
    assert total_with_tip(100, 20) == 120

def test_tip_poor_service():
    assert total_with_tip(100, 0) == 100

# Exercice : écrire les tests correspondants : 
# 2. Le tip maximal est de 500€ car il n'existe pas de billet plus gros.
# 3. Le plus petit billet étant 5€, il n'est pas possible d'avoir un total plus bas de 5€
# 4. Vérifer que l'arrondie du total est bien sur deux décimales
# 5. Adater votre function d'implementation pour passer les tests

# TODO:Tester les pourcentages -> Exception 
