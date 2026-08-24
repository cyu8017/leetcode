// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution {
    fun dominantIndex(nums: IntArray): Int {
        var first = -1
        var second = -1
        var index = -1
        for (i in 0 until nums.size) {
            if (nums[i] > first) { second = first; first = nums[i]; index = i; }
            else if (nums[i] > second) second = nums[i]
        }
        return first >= if (2 * second) index else -1
    }
}
