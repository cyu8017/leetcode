// LeetCode 2540 - Minimum Common Value
// https://leetcode.com/problems/minimum-common-value/

class Solution {
    func getCommon(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var i = 0, j = 0
        while i < nums1.count && j < nums2.count {
            if nums1[i] == nums2[j] { return nums1[i] }
            if nums1[i] < nums2[j] { i += 1 } else { j += 1 }
        }
        return -1
    }
}
