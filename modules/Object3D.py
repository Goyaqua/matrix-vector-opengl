# CENG 487 Assignment1 by
# Goyaqua
# StudentId: 
# 03/2025

import numpy as np
from modules.Vec3D import Vec3D
from modules.Mat3D import Mat3D

class Object3D:
    def __init__(self, vertices):
        self.vertices = vertices  # List of vec3D objects
        self.transformation_stack = []  # Stack of (label, Mat3D) transformations

    # Add a translation to the stack
    def push_translation(self, x, y, z):
        mat = Mat3D.translation(Vec3D(x, y, z, 1))
        self.transformation_stack.append(("T", mat))

    # Add rotation around X axis
    def push_rotation_x(self, angle):
        mat = Mat3D.rotation_x(angle)
        self.transformation_stack.append(("RX", mat))

    # Add rotation around Y axis
    def push_rotation_y(self, angle):
        mat = Mat3D.rotation_y(angle)
        self.transformation_stack.append(("RY", mat))

    # Add rotation around Z axis
    def push_rotation_z(self, angle):
        mat = Mat3D.rotation_z(angle)
        self.transformation_stack.append(("RZ", mat))

    # Add free rotation (free rotation)
    def push_free_rotation(self, axis_vec3d, angle):
        mat = Mat3D.free_rotation(axis_vec3d, angle)
        self.transformation_stack.append(("FR", mat))

    # Add a scaling transformation
    def push_scaling(self, sx, sy, sz):
        mat = Mat3D.scaling(Vec3D(sx, sy, sz, 0))
        self.transformation_stack.append(("S", mat))

    # Remove last transformation from the stack
    def pop_transformation(self):
        if self.transformation_stack:
            self.transformation_stack.pop()

    # Clear all transformations
    def clear_transformations(self):
        self.transformation_stack.clear()

    # Combine all transformations into a single matrix
    def get_transformation_matrix(self):
        matrix = Mat3D.identity()
        for label, mat in self.transformation_stack:
            matrix = mat * matrix
        return matrix

    # Return list of transformed vertices
    def transformed_vertices(self):
        transform = self.get_transformation_matrix()
        return [transform * v for v in self.vertices]

    # Print the transformation stack with labels
    def print_stack(self):
        print("Transformation Stack:")
        for label, mat in self.transformation_stack:
            print(f"{label}:\n{mat}\n")

    # String representation: print transformed vertices and stack
    def __str__(self):
        result = "Object3D Vertices (Transformed):\n"
        for i, v in enumerate(self.transformed_vertices()):
            result += f"  Vertex {i+1}: {v}\n"
        result += "\nTransformation Stack (Applied in Order):\n"
        for label, _ in self.transformation_stack:
            result += f"  {label}\n"
        return result

    # Helper methods for common transformations
    def translate(self, x, y, z):
        self.push_translation(x, y, z)

    def rotate_x(self, angle):
        self.push_rotation_x(angle)

    def rotate_y(self, angle):
        self.push_rotation_y(angle)

    def rotate_z(self, angle):
        self.push_rotation_z(angle)

    def free_rotate(self, axis_vec3d, angle):
        self.push_free_rotation(axis_vec3d, angle)

    def scale(self, sx, sy, sz):
        self.push_scaling(sx, sy, sz)