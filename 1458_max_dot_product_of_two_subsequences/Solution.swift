// LeetCode 1458 - Max Dot Product of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

class Solution {
    func maxDotProduct(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums2.count
        var dp = Array(repeating: Int.min / 4, count: n + 1)
        for a in nums1 {
            var prev = dp
            for (j, b) in nums2.enumerated() {
                let jj = j + 1
                let product = a * b
                dp[jj] = max(dp[jj - 1], prev[jj], product, product + max(0, prev[jj - 1]))
            }
        }
        return dp[n]
    }
}
