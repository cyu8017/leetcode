// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

class Solution {
    fun applyOperations(nums: IntArray): IntArray {
        val n = nums.size
        for (i in 0 until n - 1) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2
                nums[i + 1] = 0
            }
        }
        val ans = IntArray(n)
        var j = 0
        for (x in nums) if (x != 0) ans[j++] = x
        return ans
    }
}
