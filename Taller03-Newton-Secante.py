
# Taller 03: Newton y Secante en Python
# Autor: Nikolai Ortega


# EJERCICIO 1: METODO DE NEWTON

def newton_raphson(f, df, p0, TOL=1e-6, N0=50):
    historia = [p0]
    i = 1

    while i <= N0:
        d = df(p0)

        if d == 0:
            raise ZeroDivisionError("La derivada es cero")

        p = p0 - f(p0) / d
        historia.append(p)

        if abs(p - p0) < TOL:
            return p, historia

        i = i + 1
        p0 = p

    raise RuntimeError(f"El metodo fracaso despues de {N0} iteraciones")


# EJERCICIO 2: METODO DE LA SECANTE

def secante(f, p0, p1, TOL=1e-6, N0=50):
    historia = [p0, p1]
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while i <= N0:
        if q1 == q0:
            raise ZeroDivisionError("Secante horizontal: q1 == q0")

        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        historia.append(p)

        if abs(p - p1) < TOL:
            return p, historia

        i = i + 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)

    raise RuntimeError(f"El metodo fracaso despues de {N0} iteraciones")


# EJERCICIO 3: PRESTAMO BANCARIO

def saldo_final(i, monto=20000.0, cuota=450.0, meses=60):
    saldo = monto

    for mes in range(meses):
        saldo = saldo * (1 + i) - cuota

    return saldo


# PRUEBAS DE LOS TRES EJERCICIOS

def f(x):
    return x**3 + 4*x**2 - 10

def df(x):
    return 3*x**2 + 8*x


# Prueba de Newton
p, historia = newton_raphson(f, df, 1.5)
print("Newton:", round(p, 6))
print("Historia Newton:", historia)


# Prueba de la secante
llamadas = []

def f_conteo(x):
    llamadas.append(x)
    return f(x)

p, historia = secante(f_conteo, 1.0, 2.0)
print("Secante:", round(p, 6))
print("Historia Secante:", historia)
print("Evaluaciones de f:", len(llamadas))


# Prueba del prestamo
print("Saldo sin interes:", saldo_final(0))

i, historia = secante(saldo_final, 0.005, 0.02, TOL=1e-10)
print("Tasa mensual:", round(i * 100, 4), "%")
print("Tasa efectiva anual:", round(((1 + i)**12 - 1) * 100, 2), "%")
