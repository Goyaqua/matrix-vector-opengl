# CENG 487 Assignment1 by
# Goyaqua
# StudentId: 
# 03/2025

import numpy as np
from modules.Vec3D import Vec3D

class Mat3D:

    def __init__(self, data):
        if data is not None:
            self.data = data
        else:
            self.data = np.identity(4, dtype=np.float32) # if no data is provided, create identity matrix

    def __repr__(self):
        return str(self.data) #numpy's str

    @classmethod
    # Create 4x4 identity matrix 
    def identity(cls):
        return cls(np.identity(4, dtype=np.float32))

    @classmethod
    def translation(cls, vec):
        mat = np.identity(4, dtype=np.float32) #Create 4x4 identity matrix
        mat[:3, 3] = vec.to_numpy()[:3] #Set the last column to the vector to create translation matrix
        return cls(mat)

    @classmethod
    def scaling(cls, vec):
        mat = np.identity(4, dtype=np.float32) #Create 4x4 identity matrix
        mat[0, 0] = vec.x
        mat[1, 1] = vec.y
        mat[2, 2] = vec.z
        return cls(mat)

    @classmethod
    def rotation_x(cls, angle):
        c, s = np.cos(angle), np.sin(angle)
        mat = np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
        return cls(mat)

    @classmethod
    def rotation_y(cls, angle):
        c, s = np.cos(angle), np.sin(angle)
        mat = np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
        return cls(mat)

    @classmethod
    def rotation_z(cls, angle):
        c, s = np.cos(angle), np.sin(angle)
        mat = np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
        return cls(mat)

    @classmethod
    def free_rotation(cls, axis, angle):
        # Rodrigues' rotation formula
        axis_np = axis.normalize().to_numpy()[:3] #Normalize the axis vector
        x, y, z = axis_np #Get the x, y, z values of the axis vector
        cos, sin = np.cos(angle), np.sin(angle) #Get the cos and sin values of the angle
        t = 1 - cos 

        mat = np.array([
            [cos + x*x*t, x*y*t - z*sin, x*z*t + y*sin, 0],
            [y*x*t + z*sin, cos + y*y*t, y*z*t - x*sin, 0],
            [z*x*t - y*sin, z*y*t + x*sin, cos + z*z*t, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)

        return cls(mat)

    def transpose(self):
        return Mat3D(self.data.T) #numpy's transpose

    def inverse(self): #Inverse of a matrix (undo)
        return Mat3D(np.linalg.inv(self.data)) #numpy's inverse

    def __mul__(self, other):
        if isinstance(other, Mat3D): #Matrix multiplication
            return Mat3D(np.dot(self.data, other.data))
        elif isinstance(other, Vec3D): #Matrix-vector multiplication
            result = np.dot(self.data, other.to_numpy())
            return Vec3D(result[0], result[1], result[2], result[3])
        else:
            raise TypeError("Unsupported multiplication type")


    