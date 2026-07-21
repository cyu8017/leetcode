// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution {
    fun countNicePairs(nums: IntArray): Int {
        val mod = 1_000_000_007
        val freq = HashMap<Int, Int>()
        var ans = 0
        for (num in nums) {
            val diff = num - rev(num)
            ans = (ans + (freq[diff] ?: 0)) % mod
            freq[diff] = (freq[diff] ?: 0) + 1
        }
        return ans
    }

    private fun rev(x: Int): Int {
        var n = x
        var result = 0
        while (n > 0) {
            result = result * 10 + n % 10
            n /= 10
        }
        return result
    }
}
