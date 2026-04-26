import matplotlib.pyplot as plt
import numpy as np

def calcular_log(base, x):
    if base <= 0 or base == 1 or x <= 0:
        return None

    return np.log(x) / np.log(base)

try:
    base = float(input("Insira a base da função logarítmica (Obs: a > 0; a != 1): "))
    if base <= 0 or base == 1:
        print("Erro: A base deve ser positiva e diferente de 1.")
        exit()
except ValueError:
    print("Números imaginários ou incógnitas não serão considerados, por favor, insira um número válido.")
    exit()

valores_x = [3, 2, 1, 0, -1, -2, -3]

print(f"\nTabulação para y = log_{base}(x):")
print(f"{'x':>5} | {'y':>10}")
print("-" * 18)
for x in valores_x:
    y = calcular_log(base, x)
    res_str = f"{y:.4f}" if y is not None else "Indefinido."
    print(f"{x:>5} | {res_str:>10}")

x_grafico = np.linspace(0.1, 10, 400)
y_grafico = [calcular_log(base, val) for val in x_grafico]

plt.figure(figsize=(8, 5))
plt.plot(x_grafico, y_grafico, label=f'f(x) = log_{base}(x)', color='blue', linewidth=2)

x_pontos = [3, 2, 1]
y_pontos = [calcular_log(base, p) for p in x_pontos]
plt.scatter(x_pontos, y_pontos, color='#32CD32', zorder=5)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title(f"Gráfico da Função Logarítmica  de base {base}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()