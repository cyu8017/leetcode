// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

class Solution {
    func transpose(_ matrix: [[Int]]) -> [[Int]] {
        let m = matrix.count, n = matrix[0].count
        var ans = Array(repeating: Array(repeating: 0, count: m), count: n)
        for i in 0..<m {
            for j in 0..<n { ans[j][i] = matrix[i][j] }
        }
        return ans
    }
}
