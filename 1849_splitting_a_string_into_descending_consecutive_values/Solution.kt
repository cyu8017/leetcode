// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

import java.math.BigInteger

class Solution {
    fun splitString(s: String): Boolean {
        val n = s.length

        fun dfs(index: Int, previous: BigInteger?, parts: Int): Boolean {
            if (index == n) return parts >= 2
            for (end in index + 1..n) {
                val value = BigInteger(s.substring(index, end))
                if (previous == null) {
                    if (dfs(end, value, parts + 1)) return true
                } else {
                    val expected = previous.subtract(BigInteger.ONE)
                    val cmp = value.compareTo(expected)
                    if (cmp == 0) {
                        if (dfs(end, value, parts + 1)) return true
                    } else if (cmp > 0) {
                        break
                    }
                }
            }
            return false
        }

        return dfs(0, null, 0)
    }
}
