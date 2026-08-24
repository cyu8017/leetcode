// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

class Solution {
    func numberOfWays(_ n: Int, _ x: Int) -> Int {
        let MOD = 1_000_000_007
        var powers: [Int] = []
        var i = 1
        while true {
            var p = 1
            var overflow = false
            for _ in 0..<x {
                if p > n / i { overflow = true; break }
                p *= i
            }
            if overflow || p > n { break }
            powers.append(p)
            i += 1
        }
        var dp = Array(repeating: 0, count: n + 1)
        dp[0] = 1
        for p in powers {
            for s in stride(from: n, through: p, by: -1) {
                dp[s] = (dp[s] + dp[s - p]) % MOD
            }
        }
        return dp[n]
    }
}
