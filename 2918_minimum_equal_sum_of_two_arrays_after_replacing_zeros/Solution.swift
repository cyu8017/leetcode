// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution {
    func minSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var s1 = 0, s2 = 0, z1 = 0, z2 = 0
        for v in nums1 {
            if v == 0 {
                z1 += 1
                s1 += 1
            } else {
                s1 += v
            }
        }
        for v in nums2 {
            if v == 0 {
                z2 += 1
                s2 += 1
            } else {
                s2 += v
            }
        }
        if z1 == 0 && s1 < s2 { return -1 }
        if z2 == 0 && s2 < s1 { return -1 }
        return max(s1, s2)
    }
}
