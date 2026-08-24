// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

class Solution {
    func modifiedMatrix(_ matrix: [[Int]]) -> [[Int]] {
        var matrix = matrix
        let m = matrix.count, n = matrix[0].count
        for j in 0..<n {
            var mx = -1
            for i in 0..<m { mx = max(mx, matrix[i][j]) }
            for i in 0..<m where matrix[i][j] == -1 {
                matrix[i][j] = mx
            }
        }
        return matrix
    }
}
