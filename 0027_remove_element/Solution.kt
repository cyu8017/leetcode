// LeetCode 0027 - Remove Element
// https://leetcode.com/problems/remove-element/

class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var write = 0
        for (read in nums.indices) {
            if (nums[read] != `val`) {
                nums[write] = nums[read]
                write++
            }
        }
        return write
    }
}
