// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

class Solution {
    fun distinctSubseqII(s: String): Int {
        val MOD = 1_000_000_007
        val ends = LongArray(26)
        var total = 1L
        for (ch in s) {
            val prev = ends[ch - 'a']
            ends[ch - 'a'] = total
            total = (total - prev + ends[ch - 'a'] + MOD) % MOD
        }
        return ((total - 1 + MOD) % MOD).toInt()
    }
}
