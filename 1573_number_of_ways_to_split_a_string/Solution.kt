// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

class Solution {
    fun numWays(s: String): Int {
        val mod = 1_000_000_007
        var ones = 0
        for (ch in s) if (ch == '1') ones++
        if (ones % 3 != 0) return 0
        if (ones == 0) {
            val gaps = s.length - 1L
            return (gaps * (gaps - 1) / 2 % mod).toInt()
        }
        val target = ones / 3
        val positions = mutableListOf<Int>()
        for (i in s.indices) if (s[i] == '1') positions.add(i)
        val result = 1L * (positions[target] - positions[target - 1]) *
            (positions[2 * target] - positions[2 * target - 1])
        return (result % mod).toInt()
    }
}
