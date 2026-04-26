import matplotlib.pyplot as plt
import numpy as np

def analisar_e_calcular(a, x_val):
   
    if a < 0:
        return None, "Raiz imaginária/Indefinida"
    elif a == 0:
        if x_val > 0: return 0, "Constante (y=0)"
        else: return None, "Não existe"
    
    y = a ** x_val
    return y, "Ok"

base = float(input("Insira a base (a): "))
valores_x = [3, 2, 1, 0, -1, -2, -3]
valores_y = []

print(f"\nTabulação para y = {base}^x:")
print(f"{'x':>5} | {'y':>10}")
print("-" * 18)

for x in valores_x:
    y, status = analisar_e_calcular(base, x)
    
    if y is not None:
        valores_y.append(y)
        print(f"{x:>5} | {y:>10.4f}")
    else:
        valores_y.append(np.nan) 
        print(f"{x:>5} | {status}")

x_grafico = np.linspace(-3, 3, 100)
y_grafico = [base ** val if base > 0 else np.nan for val in x_grafico]

plt.plot(x_grafico, y_grafico, label=f'f(x) = {base}^x')
plt.scatter(valores_x, [base**x if base > 0 else 0 for x in valores_x], color='red')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title(f"Gráfico da Função Exponencial de base {base}")
plt.grid(True)
plt.legend()
plt.show()