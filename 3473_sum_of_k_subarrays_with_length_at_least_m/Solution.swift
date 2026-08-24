// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

class Solution {
    func maxSum(_ nums: [Int], _ k: Int, _ m: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        let neg = -(1 << 60)
        var dp = Array(repeating: Array(repeating: neg, count: n + 1), count: k + 1)
        for i in 0...n { dp[0][i] = 0 }
        if k >= 1 {
            for t in 1...k {
                var best = neg
                if t * m <= n {
                    for i in (t * m)...n {
                        let j = i - m
                        best = max(best, dp[t - 1][j] - pref[j])
                        dp[t][i] = best + pref[i]
                    }
                }
                for i in 1...n { dp[t][i] = max(dp[t][i], dp[t][i - 1]) }
            }
        }
        return dp[k][n]
    }
}
