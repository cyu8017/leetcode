// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/


class Solution {
    fun findDerangement(n: Int): Int {
        val MOD = 1_000_000_007L
        if (n == 0) return 1
        if (n == 1) return 0
        var prev2 = 1L
        var prev1 = 0L
        for (i in 2..n) {
            val cur = ((i - 1) * ((prev1 + prev2) % MOD)) % MOD
            prev2 = prev1
            prev1 = cur
        }
        return prev1.toInt()
    }
}
