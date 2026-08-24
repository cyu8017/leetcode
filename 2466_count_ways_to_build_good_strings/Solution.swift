// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution {
    func countGoodStrings(_ low: Int, _ high: Int, _ zero: Int, _ one: Int) -> Int {
        let mod = 1_000_000_007
        var dp = [Int](repeating: 0, count: high + 1)
        dp[0] = 1
        var ans = 0
        for i in 1...high {
            if i >= zero { dp[i] = (dp[i] + dp[i - zero]) % mod }
            if i >= one { dp[i] = (dp[i] + dp[i - one]) % mod }
            if i >= low { ans = (ans + dp[i]) % mod }
        }
        return ans
    }
}
