// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        if nums1.count * 6 < nums2.count || nums2.count * 6 < nums1.count {
            return -1
        }
        var s1 = nums1.reduce(0, +)
        var s2 = nums2.reduce(0, +)
        if s1 == s2 {
            return 0
        }
        var big = nums1
        var small = nums2
        if s1 < s2 {
            swap(&big, &small)
            swap(&s1, &s2)
        }
        var diff = s1 - s2
        let gains = (big.map { $0 - 1 } + small.map { 6 - $0 }).sorted(by: >)
        var ops = 0
        for gain in gains {
            if diff <= 0 {
                break
            }
            diff -= gain
            ops += 1
        }
        return diff <= 0 ? ops : -1
    }
}
