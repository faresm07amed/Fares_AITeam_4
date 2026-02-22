def matsum(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        result.append(row)
    return result

def matsub(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] - arr2[i][j])
        result.append(row)
    return result

def matmul(arr1, arr2):
    # For matrix multiplication, we create an empty result matrix filled with 0s
    result = []
    for i in range(len(arr1)):
        row = [0] * len(arr2[0])
        result.append(row)
        
    # Standard matrix dot product logic
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result

def scalarsum(scalar, arr):
    result = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[0])):
            row.append(arr[i][j] + scalar)
        result.append(row)
    return result

def scalarsub(scalar, arr):
    result = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[0])):
            row.append(arr[i][j] - scalar)
        result.append(row)
    return result

def scalarmul(scalar, arr):
    result = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[0])):
            row.append(arr[i][j] * scalar)
        result.append(row)
    return result

def matnorm(arr):
    # find the minimum and maximum values in the entire matrix
    min_val = arr[0][0]
    max_val = arr[0][0]
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] < min_val:
                min_val = arr[i][j]
            if arr[i][j] > max_val:
                max_val = arr[i][j]
                
    #  create the normalized matrix
    result = []
    range_val = max_val - min_val
    
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[0])):
            # If all numbers in the matrix are the same, avoid dividing by zero
            if range_val == 0:
                row.append(0)
            else:
                norm_value = (arr[i][j] - min_val) / range_val
                row.append(norm_value)
        result.append(row)
        
    return result

    # 1. Define two simple 2x2 matrices to test with
matrix_A = [[1, 2], 
            [3, 4]]

matrix_B = [[5, 6], 
            [7, 8]]

# 2. Call the functions and print the results
print("--- Matrix Calculator Results ---")

print("\n1. Matrix Sum (A + B):")
print(matsum(matrix_A, matrix_B))

print("\n2. Matrix Subtraction (A - B):")
print(matsub(matrix_A, matrix_B))

print("\n3. Matrix Multiplication (A * B):")
print(matmul(matrix_A, matrix_B))

print("\n4. Scalar Sum (A + 10):")
print(scalarsum(10, matrix_A))

print("\n5. Scalar Subtraction (A - 2):")
print(scalarsub(2, matrix_A))

print("\n6. Scalar Multiplication (A * 5):")
print(scalarmul(5, matrix_A))

print("\n7. Matrix Normalization of A:")
print(matnorm(matrix_A))