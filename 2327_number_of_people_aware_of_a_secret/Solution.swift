// LeetCode 2327 - Number of People Aware of a Secret
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

class Solution {
    func peopleAwareOfSecret(_ n: Int, _ delay: Int, _ forget: Int) -> Int {
        let mod = 1_000_000_007
        var dp = [Int](repeating: 0, count: n + 1)
        dp[1] = 1
        var share = 0
        if n >= 2 {
            for day in 2...n {
                if day - delay >= 1 { share = (share + dp[day - delay]) % mod }
                if day - forget >= 1 { share = (share - dp[day - forget] + mod) % mod }
                dp[day] = share
            }
        }
        var ans = 0
        for day in (n - forget + 1)...n where day >= 1 {
            ans = (ans + dp[day]) % mod
        }
        return ans
    }
}
