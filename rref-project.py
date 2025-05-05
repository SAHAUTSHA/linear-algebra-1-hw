#!/usr/bin/env python3

"""
RREF Project - Linear Algebra 1
This script allows the user to input a matrix and returns its Reduced Row Echelon Form (RREF).
Uses sympy for symbolic computation.
Author: Utsha Saha
Course: Linear Algebra 1
"""

def rref(matrix): # RREF Algorithm / Function
    rows = len(matrix)
    cols = len(matrix[0])
    lead = 0

    for r in range(rows):
        if lead >= cols:
            return matrix
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead:
                    return matrix
        # Swap rows
        matrix[i], matrix[r] = matrix[r], matrix[i]

        # Normalize row
        lv = matrix[r][lead]
        matrix[r] = [m / lv for m in matrix[r]]

        # Eliminate other rows
        for i in range(rows):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]

        lead += 1
    return matrix

def get_user_matrix(): # Function to enter Matrix
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []

    for i in range(rows): 
        while True:
            row_input = input(f"Please enter Row {i+1}'s values: ")
            try:
                row = list(map(float, row_input.strip().split()))
                if len(row) != cols:
                    print(f"Error: Not enough values inputted, expected {cols} values. Try again.") # Error Handling
                    continue
                matrix.append(row)
                break
            except ValueError: # Error Handling
                print("Error: Please enter valid numbers.")

    return matrix

def print_matrix(matrix, title="Matrix"): # Print Matrix Function 
    print(f"\n{title}:")
    for row in matrix:
        print("  ", ["{0:6.2f}".format(val) for val in row])

def main(): # Main Function 
    print("=== RREF Calculator ===")
    matrix = get_user_matrix()
    print_matrix(matrix, title="Original Matrix")

    rref_matrix = rref(matrix)
    print_matrix(rref_matrix, title="RREF Matrix")

if __name__ == "__main__":
    main()
