// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

class Solution {
    fun processStr(s: String, k: Long): Char {
        var m = 0L
        var kk = k
        for (c in s) {
            when {
                c == '*' -> m = if (m > 0) m - 1 else 0
                c == '#' -> m = m shl 1
                c != '%' -> m += 1
            }
        }
        if (kk >= m) return '.'
        var i = s.length - 1
        while (true) {
            val c = s[i]
            when (c) {
                '*' -> m += 1
                '#' -> {
                    m /= 2
                    if (kk >= m) kk -= m
                }
                '%' -> kk = m - 1 - kk
                else -> {
                    m -= 1
                    if (kk == m) return c
                }
            }
            i--
        }
    }
}
