// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

class Solution {
    func rearrangeSticks(_ n: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        if k == 0 || k > n {
            return 0
        }

        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: n + 1)
        dp[1][1] = 1

        for sticks in 2...n {
            dp[sticks][1] = (sticks - 1) * dp[sticks - 1][1] % mod
            for visible in 2...sticks {
                dp[sticks][visible] = (
                    dp[sticks - 1][visible - 1] + (sticks - 1) * dp[sticks - 1][visible]
                ) % mod
            }
        }

        return dp[n][k]
    }
}
