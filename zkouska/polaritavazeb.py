a = float(input("X(1) = "))
b = float(input("\u03A7(2) = "))

delta = abs(a - b)

if delta < 0.4:
    print("Tato vazba je nepolární.")
elif delta == 0.4:
    print("Tato vazba je slabě polární.")
elif delta > 1.7:
    print("Tato vazba je polární")
elif delta == 1.7:
    print("Tato vazba je silně polární.")
else:
    print("Tato vazba je iontová.")
