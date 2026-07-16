// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

class Solution {
    fun reversePairs(nums: IntArray): Int = mergeSort(nums, 0, nums.lastIndex)

    private fun mergeSort(nums: IntArray, start: Int, end: Int): Int {
        if (start >= end) return 0
        val mid = (start + end) / 2
        var count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end)
        var j = mid + 1
        for (i in start..mid) {
            while (j <= end && nums[i] > 2L * nums[j]) j++
            count += j - (mid + 1)
        }
        val slice = nums.copyOfRange(start, end + 1).sorted()
        for (index in slice.indices) {
            nums[start + index] = slice[index]
        }
        return count
    }
}
