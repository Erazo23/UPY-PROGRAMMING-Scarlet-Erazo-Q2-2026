import math

# # INPUT
print("1. x^2-4x+3 | 2. 3x^3-5x^2+2x-1 | 3. sin(x) | 4. cos(x) | 5. e^x | 6. ln(x)")
opc = int(input("Función: "))
a = float(input("a: "))
b = float(input("b: "))
print("1. Default (n=100, Mid) | 2. Custom | 3. Auto-adjust")
modo = int(input("Modo: "))

n, met, umbral = 100, "MIDPOINT", 0.001
if modo == 2:
    n = int(input("n: "))
    met = input("Método (LRM, RRM, MIDPOINT, TRAPEZOID): ").upper()
elif modo == 3:
    umbral = float(input("Error máximo: "))
    n, met = 10, "MIDPOINT"

# # PROCESS
# Evaluación analítica exacta (F(b) - F(a))
F = lambda x: (x**3/3 - 2*x**2 + 3*x) if opc==1 else (3/4*x**4 - 5/3*x**3 + x**2 - x) if opc==2 else -math.cos(x) if opc==3 else math.sin(x) if opc==4 else math.exp(x) if opc==5 else (x*math.log(x) - x)
v_exacto = F(b) - F(a)

# Función matemática seleccionada f(x)
f = lambda x: (x**2 - 4*x + 3) if opc==1 else (3*x**3 - 5*x**2 + 2*x - 1) if opc==2 else math.sin(x) if opc==3 else math.cos(x) if opc==4 else math.exp(x) if opc==5 else math.log(x)

while True:
    h, area = (b - a) / n, 0.0
    
    if met == "LRM" or met == "RRM":
        shift = 0 if met == "LRM" else 1
        for i in range(0 + shift, n + shift):
            area += f(a + i * h) * h
            
    elif met == "MIDPOINT":
        for i in range(n):
            area += f(a + i * h + h / 2) * h
            
    elif met == "TRAPEZOID":
        area += ((f(a) + f(b)) / 2.0) * h
        for i in range(1, n):
            area += f(a + i * h) * h

    err_abs = abs(v_exacto - area)
    err_rel = err_abs / abs(v_exacto) if v_exacto != 0 else err_abs

    if modo == 3 and err_rel > umbral and n < 100000:
        n *= 2
    else:
        break

# # OUTPUT
print("RESULTADOS FINALES")
print(f"Intervalo: [{a}, {b}] | n: {n} | Método: {met}")
print(f"Valor Exacto: {v_exacto:.6f} | Aproximado: {area:.6f}")
print(f"Error Absoluto: {err_abs:.4e} | Relativo: {err_rel:.4e} | Porcentual: {err_rel*100:.4f}%")