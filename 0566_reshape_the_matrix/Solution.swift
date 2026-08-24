// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

class Solution {
    func matrixReshape(_ mat: [[Int]], _ r: Int, _ c: Int) -> [[Int]] {
        let rows = mat.count
        let cols = mat[0].count
        if rows * cols != r * c { return mat }
        var result = Array(repeating: Array(repeating: 0, count: c), count: r)
        var index = 0
        for i in 0..<r {
            for j in 0..<c {
                result[i][j] = mat[index / cols][index % cols]
                index += 1
            }
        }
        return result
    }
}
