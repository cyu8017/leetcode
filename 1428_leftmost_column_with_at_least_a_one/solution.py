class BinaryMatrix:
    def get(self, row, col):
        raise NotImplementedError

    def dimensions(self):
        raise NotImplementedError

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        row, col, answer = 0, cols - 1, -1
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                answer = col
                col -= 1
            else:
                row += 1
        return answer
