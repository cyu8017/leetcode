// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

class Solution {
    fun reverseSubarrays(nums: IntArray, k: Int): IntArray {
        var n = nums.size
        var m = n / k
        var i = 0
        while (i < n) {
            var lo = i
            var hi = i + m - 1
            while (lo < hi) {
                var t = nums[lo]
                nums[lo] = nums[hi]
                nums[hi] = t
                lo++
                hi--
            }
            i += m
        }
        return nums
    }
}
