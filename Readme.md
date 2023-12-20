# Setup

pip install pytest

# Lancer les tests
Pour lancer les test on utilise la commande 
```
pytest
```
- Flag Verbose permet d'avoir le mot "PASSED"
```
pytest -v
```
- Flag Statement permet d'avoir les print()/logs 
```
pytest -s 
```

# TDD - Test Driven Development

Créer une function *total_with_tip*. 
Obtenir le total qui sera laissé sur la table à la fin d'un repas.
Exemple : 
- Pour un repas à *100€* (bill), et un tips de *20%*(percentage) : Je laisse sur la table *120€*(output/return).

