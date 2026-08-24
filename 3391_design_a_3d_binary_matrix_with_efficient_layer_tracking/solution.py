# LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
# https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/


class Matrix3D:
    def __init__(self, n: int) -> None:
        self.n = n
        self.m = [[[0] * n for _ in range(n)] for _ in range(n)]
        self.ones = [0] * n

    def setCell(self, x: int, y: int, z: int) -> None:
        if self.m[x][y][z] == 0:
            self.m[x][y][z] = 1
            self.ones[x] += 1

    def unsetCell(self, x: int, y: int, z: int) -> None:
        if self.m[x][y][z] == 1:
            self.m[x][y][z] = 0
            self.ones[x] -= 1

    def largestMatrix(self) -> int:
        best = -1
        idx = 0
        for i in range(self.n):
            if self.ones[i] >= best:
                best = self.ones[i]
                idx = i
        return idx
