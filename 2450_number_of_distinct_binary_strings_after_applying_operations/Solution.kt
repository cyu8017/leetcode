// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

class Solution {
    fun countDistinctStrings(s: String, k: Int): Int {
        val mod = 1_000_000_007
        val n = s.length
        var ans = 1
        for (i in 0 until n - k + 1) ans = (ans * 2L % mod).toInt()
        return ans
    }
}
