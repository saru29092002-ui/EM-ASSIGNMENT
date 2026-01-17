def gauss_law_definition():
    print("Gauss's Law:")
    print("The total electric flux through a closed surface")
    print("is equal to the enclosed charge divided by permittivity of free space.")
    print("Mathematically: Flux = Q / epsilon0")
    print()

def gauss_law_flux(charge):
    epsilon0 = 8.854e-12
    flux = charge / epsilon0
    return flux

gauss_law_definition()

Q = float(input("Enter enclosed charge in coulomb: "))
flux = gauss_law_flux(Q)
print("Electric flux =", flux, "N m^2/C")
print()

print("Example 1: Single charge enclosed")
print("Flux =", gauss_law_flux(Q), "N m^2/C")

print()
print("Example 2: No charge enclosed")
print("Flux =", gauss_law_flux(0), "N m^2/C")

print()
print("Example 3: Multiple charges enclosed")
q1 = 2
q2 = -1
q3 = 3
total_charge = q1 + q2 + q3
print("Total enclosed charge =", total_charge, "C")
print("Flux =", gauss_law_flux(total_charge), "N m^2/C")
