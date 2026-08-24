// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

class Solution {
    func deleteString(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var lcp = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                if chars[i] == chars[j] { lcp[i][j] = lcp[i + 1][j + 1] + 1 }
            }
        }
        var dp = [Int](repeating: 1, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            var len = 1
            while i + 2 * len <= n {
                if lcp[i][i + len] >= len {
                    dp[i] = max(dp[i], 1 + dp[i + len])
                }
                len += 1
            }
        }
        return dp[0]
    }
}
