// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

class Solution {
    fun customSortString(order: String, s: String): String {
        var count = IntArray(26)
        for (ch in s.toCharArray()) { count[ch - 'a']++ }
        var sb = StringBuilder()
        for (ch in order.toCharArray()) {
            while (count[ch - 'a']-- > 0) sb.append(ch)
        }
        for (i in 0 until 26) {
            while (count[i]-- > 0) sb.append((char) ('a' + i))
        }
        return sb.toString()
    }
}
