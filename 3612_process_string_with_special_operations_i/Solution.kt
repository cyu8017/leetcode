// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution {
    fun processStr(s: String): String {
        val result = StringBuilder()
        for (c in s) {
            if (c.isLetter()) result.append(c)
            else if (c == '*') {
                if (result.isNotEmpty()) result.setLength(result.length - 1)
            } else if (c == '#') result.append(result)
            else if (c == '%') result.reverse()
        }
        return result.toString()
    }
}
