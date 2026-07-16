// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

class Solution {
    func generateMatrix(_ n: Int) -> [[Int]] {
        var matrix = Array(repeating: Array(repeating: 0, count: n), count: n)
        var top = 0
        var bottom = n - 1
        var left = 0
        var right = n - 1
        var num = 1

        while top <= bottom && left <= right {
            for col in left...right {
                matrix[top][col] = num
                num += 1
            }
            top += 1

            for row in top...bottom {
                matrix[row][right] = num
                num += 1
            }
            right -= 1

            if top <= bottom {
                for col in stride(from: right, through: left, by: -1) {
                    matrix[bottom][col] = num
                    num += 1
                }
                bottom -= 1
            }

            if left <= right {
                for row in stride(from: bottom, through: top, by: -1) {
                    matrix[row][left] = num
                    num += 1
                }
                left += 1
            }
        }

        return matrix
    }
}
