// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

class Solution {
    func distinctSequences(_ n: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        let mod = 1_000_000_007
        var dp = [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: 0, count: 7), count: 7), count: n + 1)
        for a in 1...6 { dp[1][a][0] = 1 }
        if n >= 2 {
            for i in 2...n {
                for prev in 1...6 {
                    for pprev in 0...6 where dp[i - 1][prev][pprev] != 0 {
                        for cur in 1...6 {
                            if cur == prev || cur == pprev || gcd(cur, prev) != 1 { continue }
                            dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod
                        }
                    }
                }
            }
        }
        var ans = 0
        for a in 1...6 {
            for b in 0...6 { ans = (ans + dp[n][a][b]) % mod }
        }
        return ans
    }
}
