// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

class Solution {
    fun maximumMatchingIndices(nums1: IntArray, nums2: IntArray): Int {
        var n = nums1.size
        var ans = 0
        for (shift in 0 until n) {
            var cnt = 0
            for (i in 0 until n) {
                if (nums1[(i - shift + n) % n] == nums2[i]) cnt++
            }
            if (cnt > ans) ans = cnt
        }
        return ans
    }
}
