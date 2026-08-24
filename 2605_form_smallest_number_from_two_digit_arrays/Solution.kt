// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution {
    fun minNumber(nums1: IntArray, nums2: IntArray): Int {
        var s1 = HashSet<Int>()
        var s2 = HashSet<Int>()
        for (x in nums1) { s1.add(x) }
        for (x in nums2) { s2.add(x) }
        var common = 10
        for (x in s1) { if (s2.contains(x) && x < common) common = x }
        if (common < 10) return common
        var a = 10
        var b = 10
        for (x in nums1) { if (x < a) a = x }
        for (x in nums2) { if (x < b) b = x }
        return minOf(a * 10 + b, b * 10 + a)
    }
}
