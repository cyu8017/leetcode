// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

class Solution {
    func largestSumOfAverages(_ nums: [Int], _ k: Int) -> Double {
        let n = nums.count
        var prefix = Array(repeating: 0.0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + Double(nums[i]) }
        var dp = Array(repeating: 0.0, count: n)
        for i in 0..<n { dp[i] = (prefix[i + 1] - prefix[0]) / Double(i + 1) }
        if k >= 2 {
            for groups in 2...k {
                var nxt = Array(repeating: 0.0, count: n)
                for i in (groups - 1)..<n {
                    var best = 0.0
                    for j in (groups - 2)..<i {
                        best = max(best, dp[j] + (prefix[i + 1] - prefix[j + 1]) / Double(i - j))
                    }
                    nxt[i] = best
                }
                dp = nxt
            }
        }
        return dp[n - 1]
    }
}
