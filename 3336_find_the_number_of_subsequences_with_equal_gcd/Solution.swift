// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

class Solution {
    func subsequencePairCount(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            if a == 0 { return b }
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        var maxV = 0
        for x in nums where x > maxV { maxV = x }
        var dp = Array(repeating: Array(repeating: 0, count: maxV + 1), count: maxV + 1)
        dp[0][0] = 1
        for x in nums {
            var ndp = dp
            for a in 0...maxV {
                for b in 0...maxV {
                    if dp[a][b] == 0 { continue }
                    let na = a == 0 ? x : gcd(a, x)
                    let nb = b == 0 ? x : gcd(b, x)
                    ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod
                    ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod
                }
            }
            dp = ndp
        }
        var ans = 0
        if maxV >= 1 {
            for g in 1...maxV { ans = (ans + dp[g][g]) % mod }
        }
        return ans
    }
}
