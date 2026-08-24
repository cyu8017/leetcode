// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/

class Solution {
    fun isMiddleElementUnique(nums: IntArray): Boolean {
        var mid = nums[nums.size / 2]
        var cnt = 0
        for (x in nums) {
            if (x == mid) cnt++
        }
        return cnt == 1
    }
}
