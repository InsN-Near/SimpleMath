import numpy as np
def matrix_addition(A, B):
    return np.add(A, B)
def matrix_subtraction(A, B):
    return np.subtract(A, B)
def matrix_multiplication(A, B):
    return np.dot(A, B)
def matrix_transpose(A):
    return A.T
def matrix_determinant(A):
    return np.linalg.det(A)
def matrix_inverse(A):
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "Matrix is not invertible"
def eigenvalues_eigenvectors(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors
while True:
    print("\nMatrix Operations Menu:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Matrix Inversion")
    print("7. Eigenvalues and Eigenvectors")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")
    if choice in ['1', '2', '3']:
        rows1 = int(input("Enter the number of rows for matrix A: "))
        cols1 = int(input("Enter the number of columns for matrix A: "))
        A = np.zeros((rows1, cols1))
        print("Enter the elements of matrix A (row-wise):")
        for i in range(rows1):
            A[i] = np.array(list(map(float, input().split())))
        rows2 = int(input("Enter the number of rows for matrix B: "))
        cols2 = int(input("Enter the number of columns for matrix B: "))
        B = np.zeros((rows2, cols2))
        print("Enter the elements of matrix B (row-wise):")
        for i in range(rows2):
            B[i] = np.array(list(map(float, input().split())))
        if choice == '1':
            result = matrix_addition(A, B)
        elif choice == '2':
            result = matrix_subtraction(A, B)
        elif choice == '3':
            result = matrix_multiplication(A, B)
        print("Resultant Matrix:\n", result)
    elif choice in ['4', '5', '6', '7']:
        rows = int(input("Enter the number of rows for matrix A: "))
        cols = int(input("Enter the number of columns for matrix A: "))
        A = np.zeros((rows, cols))
        print("Enter the elements of matrix A (row-wise):")
        for i in range(rows):
            A[i] = np.array(list(map(float, input().split())))
        if choice == '4':
            result = matrix_transpose(A)
        elif choice == '5':
            result = matrix_determinant(A)
        elif choice == '6':
            result = matrix_inverse(A)
        elif choice == '7':
            eigenvalues, eigenvectors = eigenvalues_eigenvectors(A)
            print("Eigenvalues:\n", eigenvalues)
            print("Eigenvectors:\n", eigenvectors)
        print("Result:\n", result)
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please try again.")
