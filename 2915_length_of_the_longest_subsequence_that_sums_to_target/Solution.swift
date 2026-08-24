// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

class Solution {
    func lengthOfLongestSubsequence(_ nums: [Int], _ target: Int) -> Int {
        var dp = Array(repeating: -1, count: target + 1)
        dp[0] = 0
        for v in nums {
            var s = target
            while s >= v {
                if dp[s - v] >= 0 {
                    dp[s] = max(dp[s], dp[s - v] + 1)
                }
                s -= 1
            }
        }
        return dp[target]
    }
}
