// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/


class Solution {
    fun maxSum(nums: IntArray, k: Int): Int {
        val mod = 1_000_000_007
        val cnt = IntArray(32)
        for (v in nums) {
            for (b in 0 until 32) if ((v and (1 shl b)) != 0) cnt[b]++
        }
        var ans = 0
        repeat(k) {
            var cur = 0
            for (b in 0 until 32) {
                if (cnt[b] > 0) {
                    cur = cur or (1 shl b)
                    cnt[b]--
                }
            }
            ans = ((ans + 1L * (cur % mod) * (cur % mod) % mod) % mod).toInt()
        }
        return ans
    }
}
