import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import fobs

parametros = {
    'funcao': fobs.ackley_function,
    'lim': fobs.limit_ackley,
    'n_dim': 2,
    'alpha': 0.01,
    'beta': 0.5,
    'delta': 0.1,
    'max_iter': 250,
    'pop_size': 10
}

# Criar os pontos no espaço de busca
x_values = np.linspace(parametros['lim'][0, 0], parametros['lim'][0, 1], 100)
y_values = np.linspace(parametros['lim'][1, 0], parametros['lim'][1, 1], 100)
X, Y = np.meshgrid(x_values, y_values)
Z = parametros['funcao']([X, Y])

# Plot 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.contour(X, Y, Z, levels=50, colors='lightgrey', offset=np.min(Z))
ax.set_title('Gráfico 3D - ackley_function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Plot 2D
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(contour)
plt.contour(X, Y, Z, colors='lightgrey', levels=10) 
ax2.set_title('Gráfico 2D - ackley_function')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

plt.tight_layout()
plt.show()
