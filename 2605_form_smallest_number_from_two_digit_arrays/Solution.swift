// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution {
    func minNumber(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let s1 = Set(nums1), s2 = Set(nums2)
        var common = 10
        for x in s1 where s2.contains(x) { common = min(common, x) }
        if common < 10 { return common }
        let a = nums1.min()!, b = nums2.min()!
        return min(a * 10 + b, b * 10 + a)
    }
}
