// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

class Solution {
    fun maxValue(nums: IntArray): IntArray {
        val n = nums.size
        val ans = IntArray(n)
        val preMax = IntArray(n)
        preMax[0] = nums[0]
        for (i in 1 until n) preMax[i] = maxOf(preMax[i - 1], nums[i])
        var sufMin = Int.MAX_VALUE / 2
        for (i in n - 1 downTo 0) {
            if (preMax[i] > sufMin) ans[i] = ans[i + 1]
            else ans[i] = preMax[i]
            sufMin = minOf(sufMin, nums[i])
        }
        return ans
    }
}
