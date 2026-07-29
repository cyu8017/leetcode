// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution {
    func minScoreTriangulation(_ values: [Int]) -> Int {
        let n = values.count
        var memo = Array(repeating: Array(repeating: -1, count: n), count: n)
        func dp(_ i: Int, _ j: Int) -> Int {
            if j - i < 2 { return 0 }
            if memo[i][j] != -1 { return memo[i][j] }
            var best = Int.max
            for k in (i + 1)..<j {
                best = min(best, dp(i, k) + values[i] * values[k] * values[j] + dp(k, j))
            }
            memo[i][j] = best
            return best
        }
        return dp(0, n - 1)
    }
}
