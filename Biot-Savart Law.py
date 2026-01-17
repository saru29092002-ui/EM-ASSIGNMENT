def print_definition():
    print("BIOT–SAVART LAW")
    print("It gives the magnetic field produced by a current-carrying conductor.")
    print()


def print_statement():
    print("STATEMENT:")
    print("The magnetic field due to a small current element is")
    print("directly proportional to current, length of element,")
    print("sine of the angle and inversely proportional to square of distance.")
    print("Mathematically: dB = (mu0 / 4π) * (I dl sinθ) / r^2")
    print()


def print_proof():
    print("PROOF IDEA:")
    print("Magnetic field increases with current and length of conductor.")
    print("It is maximum when conductor is perpendicular to the point.")
    print("It decreases as square of distance.")
    print("Combining these gives the Biot–Savart formula.")
    print()


def biot_savart(I, dl, r, sin_theta):
    mu0 = 4 * 3.1416 * 1e-7
    B = (mu0 / (4 * 3.1416)) * (I * dl * sin_theta) / (r * r)
    return B


def magnetic_field_straight_wire(I, r):
    mu0 = 4 * 3.1416 * 1e-7
    B = (mu0 * I) / (2 * 3.1416 * r)
    return B


def magnetic_field_circular_loop(I, R):
    mu0 = 4 * 3.1416 * 1e-7
    B = (mu0 * I) / (2 * R)
    return B


print_definition()
print_statement()
print_proof()

print("Example 1: Magnetic field due to small current element")
B1 = biot_savart(2, 0.05, 0.2, 1)
print("Magnetic field =", B1, "tesla")
print()

print("Example 2: Magnetic field due to long straight wire")
B2 = magnetic_field_straight_wire(3, 0.1)
print("Magnetic field =", B2, "tesla")
print()

print("Example 3: Magnetic field at centre of circular loop")
B3 = magnetic_field_circular_loop(2, 0.1)
print("Magnetic field at centre =", B3, "tesla")
