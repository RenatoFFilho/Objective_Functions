import numpy as np

def rastrigin_function(x):
    """
    Função Rastrigin para otimização.

    Parâmetros:
        x (list or numpy array): Vetor contendo as coordenadas do ponto no espaço de busca.

    Retorna:
        float: Valor da função Rastrigin para as coordenadas 'x'.
    """
    dim = len(x)
    of = 0

    for i in range(dim):
        of += 10 + (x[i] ** 2) - 10 * np.cos(2 * np.pi * x[i])

    return of

limit_rastrigin = np.array([[-5.12, 5.12]]*2)

def ackley_function(x):
    """
    Função Ackley para otimização.

    Parâmetros:
        x (list or numpy array): Vetor contendo as coordenadas do ponto no espaço de busca.

    Retorna:
        float: Valor da função Ackley para as coordenadas 'x'.
    """
    dim = len(x)
    t1 = 0
    t2 = 0

    for i in range(dim):
        t1 += x[i] ** 2
        t2 += np.cos(2 * np.pi * x[i])

    of = 20 + np.e - 20 * np.exp((t1 / dim) * -0.2) - np.exp(t2 / dim)

    return of

limit_ackley = np.array([[-32.768, 32.768]]*2)


def sphere_function(x):
    """
    Função Sphere (esfera) para otimização.
    
    Parâmetros:
        x (list or numpy array): Vetor contendo as coordenadas do ponto no espaço de busca.
        
    Retorna:
        float: Valor da função Sphere para as coordenadas 'x'.
    """
    return sum(xi**2 for xi in x)
limit_sphere = np.array([[-5.12, 5.12]]*2)

def rosenbrock_function(x):
    """
    Função Rosenbrock para otimização.

    Parâmetros:
        x (list or numpy array): Vetor contendo as coordenadas do ponto no espaço de busca.

    Retorna:
        float: Valor da função Rosenbrock para as coordenadas 'x'.
    """
    n = len(x)
    result = 0
    for i in range(n-1):
        result += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
    return result

limit_rosenbrock = np.array([[-2.12, 2.12],[-1,-3]])

def beale_function(x, y):
    """
    Função de Beale para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da função de Beale para as coordenadas (x, y).
    """
    term1 = (1.5 - x + x*y)**2
    term2 = (2.25 - x + x*y**2)**2
    term3 = (2.625 - x + x*y**3)**2
    return term1 + term2 + term3
limit_beale = np.array([[-5.12, 5.12]]*2)

def goldstein_price_function(x, y):
    """
    Função Goldstein-Price para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função Goldstein-Price para as coordenadas (x, y).
    """
    termo1 = (1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y ** 2))
    termo2 = (30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * y ** 2))
    return termo1 * termo2
limit_goldstein_price = np.array([[-5.12, 5.12]]*2)

def booth_function(x, y):
    """
    Função Booth para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função Booth para as coordenadas (x, y).
    """
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2
limit_booth = np.array([[-5.12, 5.12]]*2)


def bukin_function(x, y):
    """
    Função Bukin N.6 para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função Bukin N.6 para as coordenadas (x, y).
    """
    return 100 * np.sqrt(np.abs(y - 0.01 * x**2)) + 0.01 * np.abs(x + 10)

limit_bukin = np.array([[-15, -5], [-3, 3]])


def matyas_function(x, y):
    """
    Função Matyas para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função Matyas para as coordenadas (x, y).
    """
    return 0.26 * (x**2 + y**2) - 0.48 * x * y

# Limites do espaço de busca
limit_matyas = np.array([[-10, 10], [-10, 10]])

def levi_function(x, y):
    """
    Função Lévi N.13 para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função Lévi N.13 para as coordenadas (x, y).
    """
    return np.sin(3 * np.pi * x)**2 + (x - 1)**2 * (1 + np.sin(3 * np.pi * y)**2) + (y - 1)**2 * (1 + np.sin(2 * np.pi * y)**2)

# Limites do espaço de busca
limit_levi = np.array([[-10, 10]] * 2)

def himmelblau_function(x, y):
    """
    Função Himmelblau para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função Himmelblau para as coordenadas (x, y).
    """
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

# Limites do espaço de busca
limit_himmelblau = np.array([[-5, 5]] * 2)

def three_hump_camel_function(x, y):
    """
    Função "Three-Hump Camel" para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função "Three-Hump Camel" para as coordenadas (x, y).
    """
    return 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2

# Limites do espaço de busca
limit_three_hump_camel = np.array([[-5, 5]] * 2)

def easom_function(x, y):
    """
    Função Easom para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função Easom para as coordenadas (x, y).
    """
    return -np.cos(x) * np.cos(y) * np.exp(-(x - np.pi)**2 - (y - np.pi)**2)
# Limites do espaço de busca
limit_easom = np.array([[-10, 10]] * 2)

def cross_in_tray_function(x, y):
    """
    Função "Cross-in-Tray" para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função "Cross-in-Tray" para as coordenadas (x, y).
    """
    scaled_x = x / 100.0
    scaled_y = y / 100.0

    arg = np.abs(100 - np.sqrt(scaled_x**2 + scaled_y**2) / np.pi)
    clipped_arg = np.clip(arg, -100, 100)

    exp_term = np.exp(clipped_arg)
    return -0.0001 * (np.abs(np.sin(scaled_x) * np.sin(scaled_y) * exp_term) + 1)**0.1

# Limites do espaço de busca
limit_cross_in_tray = np.array([[-10, 10]] * 2)

def eggholder_function(x, y):
    """
    Função "Eggholder" para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função "Eggholder" para as coordenadas (x, y).
    """
    return -(y + 47) * np.sin(np.sqrt(np.abs(y + x/2 + 47)/2)) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))

# Limites do espaço de busca
limit_eggholder = np.array([[-512, 512]] * 2)

def holder_table_function(x, y):
    """
    Função "Hölder Table" para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função "Hölder Table" para as coordenadas (x, y).
    """
    return -np.abs(np.sin(x) * np.cos(y) * np.exp(np.abs(1 - np.sqrt(x**2 + y**2) / np.pi)))

# Limites do espaço de busca
limit_holder_table = np.array([[-10, 10]] * 2)

def mccormick_function(x, y):
    """
    Função "McCormick" para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função "McCormick" para as coordenadas (x, y).
    """
    return np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1

# Limites do espaço de busca
limit_mccormick = np.array([[-1.5, 4], [-3, 4]])

def schaffer_function_n2(x, y):
    """
    Função "Schaffer N. 2" para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função "Schaffer N. 2" para as coordenadas (x, y).
    """
    num = np.sin(np.sqrt(x**2 + y**2))**2 - 0.5
    den = (1 + 0.001 * (x**2 + y**2))**2
    return 0.5 + (num / den)

# Limites do espaço de busca
limit_schaffer_n2 = np.array([[-100, 100]] * 2)

def schaffer_function_n4(x, y):
    """
    Função "Schaffer N. 4" para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função "Schaffer N. 4" para as coordenadas (x, y).
    """
    num = np.cos(np.sin(np.abs(x**2 - y**2)))**2 - 0.5
    den = (1 + 0.001 * (x**2 + y**2))**2
    return 0.5 + (num / den)

# Limites do espaço de busca
limit_schaffer_n4 = np.array([[-100, 100]] * 2)

def styblinski_tang_function(x, y):
    """
    Função "Styblinski-Tang" para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.

    Retorna:
        float: Valor da Função "Styblinski-Tang" para as coordenadas (x, y).
    """
    return 0.5 * (x**4 - 16 * x**2 + 5 * x + y**4 - 16 * y**2 + 5 * y)

# Limites do espaço de busca
limit_styblinski_tang = np.array([[-5, 5]]*2)

def rosenbrock_constrained(x, y):
    """
    Função de Rosenbrock com restrições de um cubo e uma linha.

    Parâmetros:
        x (numpy array): Coordenadas x no espaço de busca.
        y (numpy array): Coordenadas y no espaço de busca.

    Retorna:
        numpy array: Valor da função de Rosenbrock com restrições para as coordenadas (x, y).
    """
    # Restrição do cubo
    outside_cube = np.logical_or(x < -1, x > 1) | np.logical_or(y < -1, y > 1)

    # Restrição da linha
    outside_line = y < -x + 1

    # Aplicar as restrições
    Z = np.where(np.logical_or(outside_cube, outside_line), np.inf, (1 - x) ** 2 + 100 * (y - x ** 2) ** 2)

    return Z

# Limites do espaço de busca para a função de Rosenbrock com restrições
limit_rosenbrock_constrained = np.array([[-1.5, 1.5], [-0.5, 2.5]])

def rosenbrock_constrained_disk(x, y):
    """
    Função de Rosenbrock com restrição a um disco.

    Parâmetros:
        x (numpy array): Coordenadas x no espaço de busca.
        y (numpy array): Coordenadas y no espaço de busca.

    Retorna:
        numpy array: Valor da função de Rosenbrock com restrição para as coordenadas (x, y).
    """
    # Raio do disco
    radius = 1.5

    # Verifica se as coordenadas estão dentro do disco
    inside_disk = x**2 + y**2 <= radius**2

    # Aplica a função de Rosenbrock somente para as coordenadas dentro do disco
    Z = np.where(inside_disk, (1 - x) ** 2 + 100 * (y - x ** 2) ** 2, np.inf)

    return Z

# Limites para a função
limit_rosenbrock_constrained_disk = np.array([[-2, 2], [-2, 2]])

def mishra_bird_constrained(x, y):
    """
    Função de Mishra's Bird com restrições.

    Parâmetros:
        x (numpy array ou float): Coordenada x no espaço de busca.
        y (numpy array ou float): Coordenada y no espaço de busca.

    Retorna:
        numpy array ou float: Valor da Função de Mishra's Bird com restrições para as coordenadas (x, y).
    """
    # Se x e y são matrizes, criamos uma matriz de mesmo shape para guardar os resultados
    term1 = np.sin(y) * np.exp((1 - np.cos(x)) ** 2)
    term2 = np.cos(x) * np.exp((1 - np.sin(y)) ** 2)
    term3 = (x - y) ** 2
    return term1 + term2 + term3

# Limites para a função
limit_mishra_bird_constrained = np.array([[-10, 0], [-6.5, 0]])

def townsend_function_modified(x, y):
    """
    Função de Townsend (modificada) para otimização.

    Parâmetros:
        x (float): Coordenada x no espaço de busca.
        y (float): Coordenada y no espaço de busca.
        a (float): Constante a.
        b (float): Constante b.
        c (float): Constante c.
        d (float): Constante d.

    Retorna:
        float: Valor da Função de Townsend (modificada) para as coordenadas (x, y).
    """
    a = 1.8 
    b = 1.8
    c = 10
    d = 10

    # Se x e y são matrizes, criamos uma matriz de mesmo shape para guardar os resultados
    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        result = np.empty_like(x)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                result[i, j] = 0.5 * ((x[i, j] - a) ** 2 + (y[i, j] - b) ** 2) - np.cos(c * (x[i, j] - a)) * np.cos(d * (y[i, j] - b)) + 1
        return result
    # Se x e y são floats, calculamos o valor único da função
    else:
        return 0.5 * ((x - a) ** 2 + (y - b) ** 2) - np.cos(c * (x - a)) * np.cos(d * (y - b)) + 1

# Limites para a função
limit_townsend_modified = np.array([[-10, 10], [-10, 10]])

def simionescu_function(x, y):
    """
    Função de Simionescu para otimização.

    Parâmetros:
        x (float ou array): Coordenada x no espaço de busca.
        y (float ou array): Coordenada y no espaço de busca.

    Retorna:
        float ou array: Valor da Função de Simionescu para as coordenadas (x, y).
    """
    result = np.zeros_like(x)

    mask1 = (-1 <= x) & (x <= 0) & (-1 <= y) & (y <= 0)
    result[mask1] = 5 * (x[mask1] + 1)**2 + 5 * (y[mask1] + 1)**2

    mask2 = (0 <= x) & (x <= 1) & (-1 <= y) & (y <= 0)
    result[mask2] = 3 * (x[mask2] - 1)**2 + 5 * (y[mask2] + 1)**2

    mask3 = (-1 <= x) & (x <= 0) & (0 <= y) & (y <= 1)
    result[mask3] = 5 * (x[mask3] + 1)**2 + 3 * (y[mask3] - 1)**2

    mask4 = (0 <= x) & (x <= 1) & (0 <= y) & (y <= 1)
    result[mask4] = 3 * (x[mask4] - 1)**2 + 3 * (y[mask4] - 1)**2

    mask5 = (-2 <= x) & (x <= -1) & (-2 <= y) & (y <= -1)
    result[mask5] = (x[mask5] + 2)**2 + 5 * (y[mask5] + 2)**2

    mask6 = (-2 <= x) & (x <= -1) & (1 <= y) & (y <= 2)
    result[mask6] = (x[mask6] + 2)**2 + 5 * (y[mask6] - 2)**2

    mask7 = (1 <= x) & (x <= 2) & (-2 <= y) & (y <= -1)
    result[mask7] = (x[mask7] - 2)**2 + 5 * (y[mask7] + 2)**2

    mask8 = (1 <= x) & (x <= 2) & (1 <= y) & (y <= 2)
    result[mask8] = (x[mask8] - 2)**2 + 5 * (y[mask8] - 2)**2

    mask9 = (-2 <= x) & (x <= -1) & (-1 <= y) & (y <= 1)
    result[mask9] = (x[mask9] + 2)**2 + 3 * y[mask9]**2

    mask10 = (1 <= x) & (x <= 2) & (-1 <= y) & (y <= 1)
    result[mask10] = (x[mask10] - 2)**2 + 3 * y[mask10]**2

    mask11 = (-1 <= x) & (x <= 1) & (-2 <= y) & (y <= -1)
    result[mask11] = 3 * x[mask11]**2 + (y[mask11] + 2)**2

    mask12 = (-1 <= x) & (x <= 1) & (1 <= y) & (y <= 2)
    result[mask12] = 3 * x[mask12]**2 + (y[mask12] - 2)**2

    return result

# Limites do espaço de busca para a função de Simionescu
limit_simionescu = np.array([[-2, 2], [-2, 2]])