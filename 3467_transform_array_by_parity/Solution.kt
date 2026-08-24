// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

class Solution {
    fun transformArray(nums: IntArray): IntArray {
        for (i in 0 until nums.size) { nums[i] %= 2 }
        var j = 0
        for (i in 0 until nums.size) {
            if (nums[i] == 0) {
                var t = nums[i]; nums[i] = nums[j]; nums[j] = t
                j = j + 1
            }
        }
        return nums
    }
}
