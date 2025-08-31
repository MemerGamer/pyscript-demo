import numpy as np
from js import document


def get_vector(A, B):
    """Calculate vector from point A to point B"""
    return tuple(B[i] - A[i] for i in range(len(A)))


def calculate_volume(A, B, C, D):
    """Calculate volume of tetrahedron given 4 vertices"""
    try:
        # Get vectors from A to other vertices
        vAB = get_vector(A, B)
        vAC = get_vector(A, C)
        vAD = get_vector(A, D)

        # Calculate cross product and dot product
        ABxAC = np.cross(vAB, vAC)
        volume = abs(np.dot(ABxAC, vAD) / 6.0)

        return volume
    except Exception as e:
        raise Exception(f"Invalid data: {str(e)}")


def convert(event=None):
    """Convert coordinates to tetrahedron volume"""
    try:
        # Get input values
        A = document.getElementById("coordinate1").value
        B = document.getElementById("coordinate2").value
        C = document.getElementById("coordinate3").value
        D = document.getElementById("coordinate4").value

        # Evaluate coordinate strings (be careful with eval in production!)
        coord_A = eval(A)
        coord_B = eval(B)
        coord_C = eval(C)
        coord_D = eval(D)

        # Calculate volume
        volume = calculate_volume(coord_A, coord_B, coord_C, coord_D)

        # Display result
        document.getElementById("result").value = f"{volume:.6f}"

    except Exception as e:
        document.getElementById("result").value = f"Invalid INPUT: {str(e)}"
