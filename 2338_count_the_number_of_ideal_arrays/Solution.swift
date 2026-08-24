// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

class Solution {
    func idealArrays(_ n: Int, _ maxValue: Int) -> Int {
        let mod = 1_000_000_007
        let maxLen = 14
        var comb = [[Int]](repeating: [Int](repeating: 0, count: maxLen + 1), count: n + 1)
        for i in 0...n {
            comb[i][0] = 1
            var j = 1
            while j <= maxLen && j <= i {
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod
                j += 1
            }
        }
        var dp = [[Int]](repeating: [Int](repeating: 0, count: maxLen + 1), count: maxValue + 1)
        for i in 1...maxValue { dp[i][1] = 1 }
        for len in 2...maxLen {
            for v in 1...maxValue {
                var m = 2 * v
                while m <= maxValue {
                    dp[m][len] = (dp[m][len] + dp[v][len - 1]) % mod
                    m += v
                }
            }
        }
        var ans = 0
        for v in 1...maxValue {
            var len = 1
            while len <= maxLen && len <= n {
                ans = (ans + dp[v][len] * comb[n - 1][len - 1] % mod) % mod
                len += 1
            }
        }
        return ans
    }
}
