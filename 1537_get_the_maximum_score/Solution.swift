// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

class Solution {
    func maxSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var i = 0, j = 0
        var first = 0, second = 0
        while i < nums1.count || j < nums2.count {
            if j == nums2.count || (i < nums1.count && nums1[i] < nums2[j]) {
                first += nums1[i]; i += 1
            } else if i == nums1.count || nums2[j] < nums1[i] {
                second += nums2[j]; j += 1
            } else {
                first = max(first, second) + nums1[i]
                second = first
                i += 1; j += 1
            }
        }
        return max(first, second) % 1_000_000_007
    }
}
