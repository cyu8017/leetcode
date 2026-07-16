// LeetCode 0048 - Rotate Image
// https://leetcode.com/problems/rotate-image/

class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let n = matrix.count

        for i in 0..<n {
            for j in (i + 1)..<n {
                let tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
            }
        }

        for i in 0..<n {
            matrix[i].reverse()
        }
    }
}
