import numpy as np
import matplotlib.pyplot as plt

# Definición de la función y su derivada analítica
def f(x):
    return np.sin(x)  # Función del ejercicio

def df_analytical(x):
    return np.cos(x)  # Derivada exacta de sin(x) es cos(x)

# Métodos de diferencias finitas
def forward_diff(f, x, h=0.1):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h=0.1):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h=0.1):
    return (f(x + h) - f(x - h)) / (2*h)

# Parámetros del ejercicio
a = 0.0
b = np.pi  # Intervalo [0, π]
h = 0.1    # Paso dado en el ejercicio

# Puntos de evaluación (usando el paso h=0.1)
x_vals = np.arange(a, b + h, h)  # Incluye el punto final π

# Derivada exacta
df_exact = df_analytical(x_vals)

# Aproximaciones numéricas
df_forward = forward_diff(f, x_vals, h)
df_backward = backward_diff(f, x_vals, h)
df_central = central_diff(f, x_vals, h)

# Errores absolutos
error_forward = np.abs(df_forward - df_exact)
error_backward = np.abs(df_backward - df_exact)
error_central = np.abs(df_central - df_exact)

# Graficar la función y sus derivadas
plt.figure(figsize=(12, 6))
plt.plot(x_vals, f(x_vals), '-', label='f(x) = sin(x)')
plt.plot(x_vals, df_exact, 'k-', label='Derivada exacta (cos(x))')
plt.plot(x_vals, df_forward, 'r--', label='Dif. hacia adelante')
plt.plot(x_vals, df_backward, 'g-.', label='Dif. hacia atrás')
plt.plot(x_vals, df_central, 'b:', label='Dif. centradas')
plt.xlabel('x')
plt.ylabel("Valor")
plt.legend()
plt.title("Comparación de Métodos de Diferenciación Numérica para sin(x)")
plt.grid()
plt.savefig("derivadas_sin(x).png")
plt.show()

# Graficar los errores
plt.figure(figsize=(12, 6))
plt.plot(x_vals, error_forward, 'r--', label='Error dif. hacia adelante')
plt.plot(x_vals, error_backward, 'g-.', label='Error dif. hacia atrás')
plt.plot(x_vals, error_central, 'b:', label='Error dif. centradas')
plt.xlabel('x')
plt.ylabel("Error absoluto")
plt.legend()
plt.title("Errores en la Aproximación de la Derivada de sin(x)")
plt.grid()
plt.savefig("errores_derivadas_sin(x).png")
plt.show()

# Mostrar resultados en una tabla para algunos puntos
print("\nResultados para algunos puntos (x ∈ [0, π]):")
print("x\tExacta\tAdelante\tAtrás\tCentrada\tError Adelante\tError Atrás\tError Centrada")
for i in range(0, len(x_vals), 5):  # Mostrar cada 5 puntos para brevedad
    x = x_vals[i]
    print(f"{x:.1f}\t{df_exact[i]:.4f}\t{df_forward[i]:.4f}\t\t{df_backward[i]:.4f}\t{df_central[i]:.4f}\t\t{error_forward[i]:.4f}\t\t{error_backward[i]:.4f}\t\t{error_central[i]:.4f}")
