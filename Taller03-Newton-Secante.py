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

def saldo_final(i, monto=20000.0, cuota=450.0, meses=60):
    saldo = monto
    for mes in range(meses):
        saldo = saldo * (1 + i) - cuota
    return saldo