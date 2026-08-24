// LeetCode 3940 - Limit Occurrences In Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/

class Solution {
    fun limitOccurrences(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        var cnt = 1
        var l = 1
        for (r in 1 until n) {
            if (nums[r] != nums[r - 1]) cnt = 1 else cnt++
            if (cnt <= k) {
                nums[l] = nums[r]
                l++
            }
        }
        return nums.copyOf(l)
    }
}
