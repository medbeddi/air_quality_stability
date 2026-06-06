import numpy as np

A = np.array([[1.0, 1.0/2.0, 1.0/3.0],
              [1.0/2.0, 1.0/3.0, 1.0/4.0],
              [1.0/3.0, 1.0/4.0, 1.0/5.0]])

b = np.array([1.0, 0.5, 0.3333])

# 1. Calcul du conditionnement
kappa_A = np.linalg.cond(A, p=2)
print(f"Conditionnement de la matrice de resolution kappa(A) = {kappa_A:.2f}")

# 2. Resolution du systeme exact (sans inversion explicite)
x_exact = np.linalg.solve(A, b)

# 3. Perturbation microscopique sur b
b_perturbe = b.copy()
b_perturbe[2] += 1e-14

x_perturbe = np.linalg.solve(A, b_perturbe)

# 4. Erreur relative
erreur_relative = np.linalg.norm(x_exact - x_perturbe) / np.linalg.norm(x_exact)
print(f"Erreur relative induite sur la prediction x : {erreur_relative:.6f}")
