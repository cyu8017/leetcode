// LeetCode 0073 - Set Matrix Zeroes
// https://leetcode.com/problems/set-matrix-zeroes/

class Solution {
    func setZeroes(_ matrix: inout [[Int]]) {
        let rows = matrix.count
        let cols = matrix[0].count
        let firstRowZero = matrix[0].contains(0)
        let firstColZero = matrix.contains { $0[0] == 0 }

        for i in 1..<rows {
            for j in 1..<cols {
                if matrix[i][j] == 0 {
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                }
            }
        }

        for i in 1..<rows {
            for j in 1..<cols {
                if matrix[i][0] == 0 || matrix[0][j] == 0 {
                    matrix[i][j] = 0
                }
            }
        }

        if firstRowZero {
            for j in 0..<cols {
                matrix[0][j] = 0
            }
        }
        if firstColZero {
            for i in 0..<rows {
                matrix[i][0] = 0
            }
        }
    }
}
