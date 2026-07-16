// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        if (nums.size <= 2) {
            return nums.size
        }

        var write = 2
        for (i in 2 until nums.size) {
            if (nums[i] != nums[write - 2]) {
                nums[write] = nums[i]
                write++
            }
        }

        return write
    }
}
