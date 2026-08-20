// LeetCode 1582 - Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution {
    func numSpecial(_ mat: [[Int]]) -> Int {
        let rows = mat.map { $0.reduce(0, +) }
        var cols = Array(repeating: 0, count: mat[0].count)
        for row in mat {
            for (j, v) in row.enumerated() { cols[j] += v }
        }
        var ans = 0
        for i in 0..<mat.count {
            for j in 0..<mat[0].count {
                if mat[i][j] == 1 && rows[i] == 1 && cols[j] == 1 { ans += 1 }
            }
        }
        return ans
    }
}
