// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution {
    func findLength(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let m = nums1.count, n = nums2.count
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        var best = 0
        for i in 1...m {
            for j in 1...n {
                if nums1[i - 1] == nums2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    best = max(best, dp[i][j])
                }
            }
        }
        return best
    }
}
