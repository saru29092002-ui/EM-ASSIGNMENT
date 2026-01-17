def definition():
    print("MAXWELL'S EQUATIONS IN THREE DIMENSIONS (3D)")
    print("They describe electric and magnetic fields")
    print("varying along x, y, z directions and time.")
    print()


def statement():
    print("STATEMENT:")
    print("1. Divergence of E = rho / epsilon0")
    print("2. Divergence of B = 0")
    print("3. Curl of E = - dB/dt")
    print("4. Curl of B = mu0*J + mu0*epsilon0*dE/dt")
    print()


def gauss_electric(rho):
    epsilon0 = 8.854e-12
    return rho / epsilon0


def gauss_magnetic():
    return 0


def faraday_law(dB_dt):
    return -dB_dt


def ampere_maxwell(J, dE_dt):
    mu0 = 4 * 3.1416 * 1e-7
    epsilon0 = 8.854e-12
    return mu0 * J + mu0 * epsilon0 * dE_dt


definition()
statement()

print("Example 1: Gauss's Law for Electricity")
rho = 2e-6
result1 = gauss_electric(rho)
print("Charge density =", rho, "C/m^3")
print("Divergence of E =", result1, "V/m^2")
print()

print("Example 2: Gauss's Law for Magnetism")
result2 = gauss_magnetic()
print("Divergence of B =", result2)
print()

print("Example 3: Faraday's Law")
dB_dt = 4
result3 = faraday_law(dB_dt)
print("Rate of change of B =", dB_dt, "T/s")
print("Curl of E =", result3)
print()

print("Example 4: Ampere-Maxwell Law")
J = 3
dE_dt = 5
result4 = ampere_maxwell(J, dE_dt)
print("Current density =", J, "A/m^2")
print("Rate of change of E =", dE_dt)
print("Curl of B =", result4)
