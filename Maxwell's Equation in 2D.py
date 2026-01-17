def definition():
    print("MAXWELL'S EQUATIONS IN TWO DIMENSIONS (2D)")
    print("They describe electric and magnetic fields")
    print("varying along x and y directions only.")
    print()


def statement():
    print("STATEMENT (2D FORM):")
    print("1. dEx/dx + dEy/dy = rho / epsilon0")
    print("2. dBz/dx = 0 and dBz/dy = 0")
    print("3. dEy/dx - dEx/dy = - dBz/dt")
    print("4. dBz/dx = mu0 * epsilon0 * dEy/dt")
    print("   dBz/dy = - mu0 * epsilon0 * dEx/dt")
    print()


def gauss_law_2d(rho):
    epsilon0 = 8.854e-12
    return rho / epsilon0


def faraday_law_2d(dEx_dy, dEy_dx):
    return dEy_dx - dEx_dy


def ampere_maxwell_2d(dE_dt):
    mu0 = 4 * 3.1416 * 1e-7
    epsilon0 = 8.854e-12
    return mu0 * epsilon0 * dE_dt


definition()
statement()

print("Example 1: Gauss's Law in 2D")
rho = 1e-6
result1 = gauss_law_2d(rho)
print("Charge density =", rho, "C/m^2")
print("dEx/dx + dEy/dy =", result1, "V/m^2")
print()

print("Example 2: Faraday's Law in 2D")
dEx_dy = 2
dEy_dx = 5
result2 = faraday_law_2d(dEx_dy, dEy_dx)
print("dEy/dx =", dEy_dx)
print("dEx/dy =", dEx_dy)
print("dBz/dt =", -result2, "T/s")
print()

print("Example 3: Ampere-Maxwell Law in 2D")
dE_dt = 4
result3 = ampere_maxwell_2d(dE_dt)
print("dE/dt =", dE_dt, "V/m·s")
print("dBz/dx or dBz/dy =", result3, "T/m")
