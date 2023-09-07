def Puissance_2(a,b):
    if not (isinstance(A, (int, float)) and isinstance(B, int)):
        raise ValueError("A doit être un nombre (int ou float) et B doit être un nombre entier.")

    if B < 0:
        raise ValueError("B doit être un nombre entier non négatif.")

    return A ** B

try:
    resultat = puissance("2", 3)
    print(f"2 à la puissance 3 est égal à : {resultat}")
except ValueError as e:
    print(f"Erreur: {e}")

try:
    resultat = puissance(2, 2.5)
    print(f"2 à la puissance 2.5 est égal à : {resultat}")
except ValueError as e:
    print(f"Erreur: {e}")

try:
    resultat = puissance(2, -3)
    print(f"2 à la puissance -3 est égal à : {resultat}")
except ValueError as e:
    print(f"Erreur: {e}")

		
	
