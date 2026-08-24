// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

class Solution {
    fun orArray(nums: IntArray): IntArray {
        var ans = IntArray(nums.size - 1)
        for (i in 1 until nums.size) { ans[i - 1] = nums[i] | nums[i - 1] }
        return ans
    }
}
