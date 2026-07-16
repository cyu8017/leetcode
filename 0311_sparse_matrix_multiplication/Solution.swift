// LeetCode 0311 - Sparse Matrix Multiplication
// https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution {
    func multiply(_ mat1: [[Int]], _ mat2: [[Int]]) -> [[Int]] {
        let rows = mat1.count
        let inner = mat1[0].count
        let cols = mat2[0].count
        var result = Array(repeating: Array(repeating: 0, count: cols), count: rows)
        for row in 0..<rows {
            for index in 0..<inner {
                if mat1[row][index] == 0 {
                    continue
                }
                for col in 0..<cols {
                    if mat2[index][col] != 0 {
                        result[row][col] += mat1[row][index] * mat2[index][col]
                    }
                }
            }
        }
        return result
    }
}
