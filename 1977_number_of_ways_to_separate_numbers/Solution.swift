// LeetCode 1977 - Number of Ways to Separate Numbers
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

class Solution {
    func numberOfCombinations(_ num: String) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(num)
        let n = chars.count
        if chars[0] == "0" { return 0 }
        var lcp = Array(repeating: Array(repeating: 0, count: n + 1), count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                if chars[i] == chars[j] {
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
                }
            }
        }
        func le(_ a: Int, _ b: Int, _ length: Int) -> Bool {
            let common = lcp[a][b]
            if common >= length { return true }
            return chars[a + common] < chars[b + common]
        }
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: n + 1)
        var pref = Array(repeating: Array(repeating: 0, count: n + 1), count: n + 1)
        for i in 1...n {
            for l in 1...i {
                let start = i - l
                if chars[start] == "0" {
                    dp[i][l] = 0
                } else if start == 0 {
                    dp[i][l] = 1
                } else {
                    var ways = l > 1 ? pref[start][min(l - 1, start)] : 0
                    if start >= l && le(start - l, start, l) {
                        ways = (ways + dp[start][l]) % MOD
                    }
                    dp[i][l] = ways
                }
            }
            for l in 1...n {
                pref[i][l] = (pref[i][l - 1] + (l <= i ? dp[i][l] : 0)) % MOD
            }
        }
        return pref[n][n]
    }
}
