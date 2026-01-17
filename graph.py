def coulomb_force(q1, q2, r):
    k = 9e9
    return k * q1 * q2 / (r * r)


q1 = 1e-6
q2 = 1e-6

print("Distance (m)    Force (N)")
print("--------------------------")

r = 0.1
while r <= 1.0:
    F = coulomb_force(q1, q2, r)
    print(r, "        ", F)
    r = r + 0.1


def coulomb_force(q1, q2, r):
    k = 9e9
    return k * q1 * q2 / (r * r)


q1 = 1e-6
q2 = 1e-6

print("Coulomb's Law: Force vs Distance")
print("Each * represents force strength")

r = 0.1
while r <= 1.0:
    F = coulomb_force(q1, q2, r)
    stars = int(F * 10)
    print("r =", r, "|", "*" * stars)
    r = r + 0.1
