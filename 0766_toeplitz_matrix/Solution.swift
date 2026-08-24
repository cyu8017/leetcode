// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

class Solution {
    func isToeplitzMatrix(_ matrix: [[Int]]) -> Bool {
        for i in 1..<matrix.count {
            for j in 1..<matrix[0].count {
                if matrix[i][j] != matrix[i - 1][j - 1] { return false }
            }
        }
        return true
    }
}
