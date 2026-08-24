// LeetCode 0026 - Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        if (nums.isEmpty()) {
            return 0
        }

        var write = 1
        for (read in 1 until nums.size) {
            if (nums[read] != nums[write - 1]) {
                nums[write] = nums[read]
                write++
            }
        }

        return write
    }
}
