// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

class Solution {
    func longestIdealString(_ s: String, _ k: Int) -> Int {
        var dp = [Int](repeating: 0, count: 26)
        var ans = 0
        for ch in s.utf8 {
            let c = Int(ch - 97)
            var best = 0
            for p in 0..<26 where abs(c - p) <= k {
                best = max(best, dp[p])
            }
            dp[c] = best + 1
            ans = max(ans, dp[c])
        }
        return ans
    }
}
