// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution {
    fun countElements(nums: IntArray): Int {
        var mn: Int = nums[0], mx = nums[0]
        for (x in nums) { mn = minOf(mn, x); mx = maxOf(mx, x); }
        var ans: Int = 0
        for (x in nums) if (x > mn && x < mx) ans++
        return ans
    }
}
