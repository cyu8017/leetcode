// LeetCode 1572 - Matrix Diagonal Sum
// https://leetcode.com/problems/matrix-diagonal-sum/

class Solution {
    func diagonalSum(_ mat: [[Int]]) -> Int {
        let n = mat.count
        var sum = 0
        for i in 0..<n {
            sum += mat[i][i] + mat[i][n - 1 - i]
        }
        if n % 2 == 1 { sum -= mat[n / 2][n / 2] }
        return sum
    }
}
