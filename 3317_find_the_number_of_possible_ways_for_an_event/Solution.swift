// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

class Solution {
    func numberOfWays(_ n: Int, _ x: Int, _ y: Int) -> Int {
        let mod = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: x + 1), count: n + 1)
        dp[0][0] = 1
        for i in 1...n {
            for j in 1...min(x, i) {
                dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j] % mod) % mod
            }
        }
        var fact = Array(repeating: 1, count: x + 1)
        if x >= 1 {
            for i in 1...x { fact[i] = fact[i - 1] * i % mod }
        }
        var ans = 0, ypow = 1
        for k in 1...min(x, n) {
            ypow = ypow * y % mod
            let perm = fact[x] * modPow(fact[x - k], mod - 2, mod) % mod
            ans = (ans + dp[n][k] * perm % mod * ypow % mod) % mod
        }
        return ans
    }

    private func modPow(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var r = 1, a = a % mod, e = e
        while e > 0 {
            if e & 1 != 0 { r = r * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return r
    }
}
