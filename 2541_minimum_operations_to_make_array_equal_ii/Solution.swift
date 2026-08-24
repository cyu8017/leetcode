// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        if k == 0 {
            return nums1 == nums2 ? 0 : -1
        }
        var pos = 0, neg = 0
        for i in 0..<nums1.count {
            let d = nums1[i] - nums2[i]
            if d % k != 0 { return -1 }
            if d > 0 { pos += d / k }
            else { neg += (-d) / k }
        }
        return pos != neg ? -1 : pos
    }
}
