// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

class Solution {
    fun makeArrayPositive(nums: IntArray): Int {
        var ans = 0
        var l = -1
        var preMx = 0
        var s = 0
        for (r in 0 until nums.size) {
            s += nums[r]
            if (r - l > 2 && s <= preMx) {
                ans = ans + 1
                l = r
                preMx = 0
                s = 0
            } else if (r - l >= 2) {
                preMx = maxOf(preMx, s - nums[r] - nums[r - 1])
            }
        }
        return ans
    }
}
