#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """Rotate a matrix 90 degrees clockwise"""
    rotated_matrix = []
    for row in range(len(matrix)):
        rotatedRow= []
        for column in range(len(matrix)-1 , -1, -1):
            rotatedRow.append(matrix[column][row])
        rotated_matrix.append(rotatedRow)


