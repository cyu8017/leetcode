// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

class Solution {
    fun maximizeGreatness(nums: IntArray): Int {
        nums.sort()
        var i = 0
        for (x in nums) {
            if (x > nums[i]) { i = i + 1 }
        }
        return i
    }
}
