# CENG 487 Assignment1 by
# Goyaqua
# StudentId: 
# 03/2025

import math
import numpy as np

class Vec3D:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def __repr__(self):
        return "Vec3D(%s, %s, %s, %s)" % (self.x, self.y, self.z, self.w)

    def __add__(self, other):
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z, self.w)
    
    def __sub__(self, other):
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z, self.w)

    def __mul__(self, constant):
        return Vec3D(self.x * constant, self.y * constant, self.z * constant, self.w)

    def __truediv__(self, constant):
        if constant == 0:
            raise ValueError("0 division error")
        return Vec3D(self.x / constant, self.y / constant, self.z / constant, self.w)

    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def normalize(self): # Unit vector
        l = self.length()
        if l == 0:
            return Vec3D(0, 0, 0, 0)
        return self / l

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x, 0)

    def angle_with(self, other):
        # cos(theta) = (a.dot(b)) / (|a|.|b|)
        return math.acos(self.dot(other) / (self.length() * other.length()))

    def project_on(self, other):
        other_norm = other.normalize()
        return self.dot(other_norm) * other_norm
    
    def to_numpy(self):
        return np.array([self.x, self.y, self.z, self.w])