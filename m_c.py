import numpy as np

print("MATRIX CALCULATOR")

# Enter matrices directly
A = np.array(eval(input("Enter Matrix A: ")))
B = np.array(eval(input("Enter Matrix B: ")))

print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Determinant of A")
print("5. Inverse of A")
print("6. Transpose of A")

choice = input("Choose operation: ")

try:
    if choice == "1":
        print("\nResult:")
        print(A + B)

    elif choice == "2":
        print("\nResult:")
        print(A - B)

    elif choice == "3":
        print("\nResult:")
        print(A @ B)

    elif choice == "4":
        print("\nDeterminant:")
        print(np.linalg.det(A))

    elif choice == "5":
        print("\nInverse:")
        print(np.linalg.inv(A))

    elif choice == "6":
        print("\nTranspose:")
        print(A.T)

    else:
        print("Invalid choice")

except Exception as e:
    print("Error:", e)
