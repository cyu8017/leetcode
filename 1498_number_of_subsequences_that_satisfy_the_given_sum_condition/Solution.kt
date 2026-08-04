// LeetCode 1498 - Number of Subsequences That Satisfy the Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution {
    fun numSubseq(nums: IntArray, target: Int): Int {
        nums.sort()
        val mod = 1_000_000_007
        val powers = IntArray(nums.size + 1)
        powers[0] = 1
        for (i in 1 until powers.size) powers[i] = (powers[i - 1] * 2) % mod
        var left = 0
        var right = nums.size - 1
        var ans = 0
        while (left <= right) {
            if (nums[left] + nums[right] <= target) {
                ans = (ans + powers[right - left]) % mod
                left++
            } else {
                right--
            }
        }
        return ans
    }
}
