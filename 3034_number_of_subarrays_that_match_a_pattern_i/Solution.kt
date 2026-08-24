// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

class Solution {
    private fun f(a: Int, b: Int): Int {
        if (a == b) return 0
        return if (a < b) 1 else -1
    }

    fun countMatchingSubarrays(nums: IntArray, pattern: IntArray): Int {
        val n = nums.size
        val m = pattern.size
        var ans = 0
        for (i in 0 until n - m) {
            var ok = 1
            var k = 0
            while (k < m && ok != 0) {
                if (f(nums[i + k], nums[i + k + 1]) != pattern[k]) ok = 0
                k++
            }
            ans += ok
        }
        return ans
    }
}
