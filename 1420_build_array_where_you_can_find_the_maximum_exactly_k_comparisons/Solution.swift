// LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
// https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

class Solution {
    func numOfArrays(_ n: Int, _ m: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        var dp = Array(repeating: Array(repeating: 0, count: m + 1), count: k + 1)
        for maximum in 1...m { dp[1][maximum] = 1 }
        for _ in 1..<n {
            var nxt = Array(repeating: Array(repeating: 0, count: m + 1), count: k + 1)
            for cost in 1...k {
                var prefix = 0
                for maximum in 1...m {
                    prefix = (prefix + dp[cost - 1][maximum - 1]) % mod
                    nxt[cost][maximum] = (maximum * dp[cost][maximum] + prefix) % mod
                }
            }
            dp = nxt
        }
        return dp[k].reduce(0, +) % mod
    }
}
