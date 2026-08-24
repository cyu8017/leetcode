// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

class Solution {
    fun sortArray(nums: IntArray): IntArray {
        if (nums.size <= 1) return nums
        var mid = nums.size / 2
        var left = Arrays.copyOfRange(nums, 0, mid)
        var right = Arrays.copyOfRange(nums, mid, nums.size)
        left = sortArray(left)
        right = sortArray(right)
        var merged = IntArray(nums.size)
        var i = 0
        var j = 0
        var k = 0
        while (i < left.size && j < right.size) {
            if (left[i] <= right[j]) merged[k++] = left[i++]
            else merged[k++] = right[j++]
        }
        while (i < left.size) merged[k++] = left[i++]
        while (j < right.size) merged[k++] = right[j++]
        return merged
    }
}
