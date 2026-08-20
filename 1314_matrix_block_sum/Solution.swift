// LeetCode 1314 - Matrix Block Sum
// https://leetcode.com/problems/matrix-block-sum/

class Solution {
    func matrixBlockSum(_ mat: [[Int]], _ k: Int) -> [[Int]] {
        let m = mat.count, n = mat[0].count
        var prefix = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for r in 0..<m {
            for c in 0..<n {
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
            }
        }
        var answer = Array(repeating: Array(repeating: 0, count: n), count: m)
        for r in 0..<m {
            for c in 0..<n {
                let r1 = max(0, r - k), c1 = max(0, c - k)
                let r2 = min(m - 1, r + k), c2 = min(n - 1, c + k)
                answer[r][c] = prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]
            }
        }
        return answer
    }
}
