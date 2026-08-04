// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

class Solution {
    fun thousandSeparator(n: Int): String {
        var s = n.toString()
        val parts = mutableListOf<String>()
        while (s.isNotEmpty()) {
            val start = maxOf(0, s.length - 3)
            parts.add(s.substring(start))
            s = s.substring(0, start)
        }
        parts.reverse()
        return parts.joinToString(".")
    }
}
