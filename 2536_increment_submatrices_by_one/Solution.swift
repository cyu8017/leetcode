// LeetCode 2536 - Increment Submatrices by One
// https://leetcode.com/problems/increment-submatrices-by-one/

class Solution {
    func rangeAddQueries(_ n: Int, _ queries: [[Int]]) -> [[Int]] {
        var diff = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: n + 1)
        for q in queries {
            let r1 = q[0], c1 = q[1], r2 = q[2], c2 = q[3]
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        }
        var mat = [[Int]](repeating: [Int](repeating: 0, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n {
                var v = diff[i][j]
                if i > 0 { v += mat[i - 1][j] }
                if j > 0 { v += mat[i][j - 1] }
                if i > 0 && j > 0 { v -= mat[i - 1][j - 1] }
                mat[i][j] = v
            }
        }
        return mat
    }
}
