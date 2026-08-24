// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

class Solution {
    func maxNonDecreasingLength(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var dp1 = 1, dp2 = 1, ans = 1
        for i in 1..<n {
            var nd1 = 1, nd2 = 1
            if nums1[i] >= nums1[i - 1] { nd1 = max(nd1, dp1 + 1) }
            if nums1[i] >= nums2[i - 1] { nd1 = max(nd1, dp2 + 1) }
            if nums2[i] >= nums1[i - 1] { nd2 = max(nd2, dp1 + 1) }
            if nums2[i] >= nums2[i - 1] { nd2 = max(nd2, dp2 + 1) }
            dp1 = nd1
            dp2 = nd2
            ans = max(ans, max(dp1, dp2))
        }
        return ans
    }
}
