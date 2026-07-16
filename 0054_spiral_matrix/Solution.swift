// LeetCode 0054 - Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        if matrix.isEmpty {
            return []
        }

        var top = 0
        var bottom = matrix.count - 1
        var left = 0
        var right = matrix[0].count - 1
        var result: [Int] = []

        while top <= bottom && left <= right {
            for col in left...right {
                result.append(matrix[top][col])
            }
            top += 1

            for row in top...bottom {
                result.append(matrix[row][right])
            }
            right -= 1

            if top <= bottom {
                for col in stride(from: right, through: left, by: -1) {
                    result.append(matrix[bottom][col])
                }
                bottom -= 1
            }

            if left <= right {
                for row in stride(from: bottom, through: top, by: -1) {
                    result.append(matrix[row][left])
                }
                left += 1
            }
        }

        return result
    }
}
