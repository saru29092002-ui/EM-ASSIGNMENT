def print_definition():
    print("MAXWELL'S EQUATIONS IN ONE DIMENSION")
    print("They describe the variation of electric and magnetic fields")
    print("along a single spatial direction (x-axis).")
    print()


def print_statement():
    print("STATEMENT (1D FORM):")
    print("1. dE/dx = rho / epsilon0")
    print("2. dB/dx = 0")
    print("3. dE/dx = - dB/dt")
    print("4. dB/dx = mu0 * epsilon0 * dE/dt")
    print()


def gauss_law_1d(rho):
    epsilon0 = 8.854e-12
    return rho / epsilon0


def faraday_law_1d(dB_dt):
    return -dB_dt


def ampere_maxwell_1d(dE_dt):
    mu0 = 4 * 3.1416 * 1e-7
    epsilon0 = 8.854e-12
    return mu0 * epsilon0 * dE_dt


print_definition()
print_statement()

print("Example 1: Gauss's Law in 1D")
rho = 2e-6
dE_dx = gauss_law_1d(rho)
print("Charge density =", rho, "C/m^3")
print("dE/dx =", dE_dx, "V/m^2")
print()

print("Example 2: Faraday's Law in 1D")
dB_dt = 0.01
dE_dx_faraday = faraday_law_1d(dB_dt)
print("dB/dt =", dB_dt, "T/s")
print("dE/dx =", dE_dx_faraday, "V/m^2")
print()

print("Example 3: Ampere-Maxwell Law in 1D")
dE_dt = 5
dB_dx = ampere_maxwell_1d(dE_dt)
print("dE/dt =", dE_dt, "V/m·s")
print("dB/dx =", dB_dx, "T/m")
