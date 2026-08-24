// LeetCode 3097 - Shortest Subarray With OR at Least K II
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution {
    fun minimumSubarrayLength(nums: IntArray, k: Int): Int {
        val n = nums.size
        val cnt = IntArray(32)
        var ans = n + 1
        var s = 0
        var i = 0
        for (j in 0 until n) {
            val x = nums[j]
            s = s or x
            for (h in 0 until 32) {
                if (((x shr h) and 1) != 0) cnt[h]++
            }
            while (s >= k && i <= j) {
                ans = minOf(ans, j - i + 1)
                for (h in 0 until 32) {
                    if (((nums[i] shr h) and 1) != 0) {
                        cnt[h]--
                        if (cnt[h] == 0) s = s xor (1 shl h)
                    }
                }
                i++
            }
        }
        return if (ans == n + 1) -1 else ans
    }
}
