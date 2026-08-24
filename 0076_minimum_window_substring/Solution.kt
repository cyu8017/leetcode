// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

class Solution {
    fun minWindow(s: String, t: String): String {
        if (t.isEmpty()) {
            return ""
        }

        val need = HashMap<Char, Int>()
        for (ch in t) {
            need[ch] = (need[ch] ?: 0) + 1
        }

        val required = need.size
        var formed = 0
        val window = HashMap<Char, Int>()
        var left = 0
        var bestLen = Int.MAX_VALUE
        var bestLeft = 0

        for (right in s.indices) {
            val ch = s[right]
            window[ch] = (window[ch] ?: 0) + 1
            if (need.containsKey(ch) && window[ch] == need[ch]) {
                formed++
            }

            while (formed == required) {
                if (right - left + 1 < bestLen) {
                    bestLen = right - left + 1
                    bestLeft = left
                }

                val leftCh = s[left]
                window[leftCh] = window[leftCh]!! - 1
                if (need.containsKey(leftCh) && window[leftCh]!! < need[leftCh]!!) {
                    formed--
                }
                left++
            }
        }

        if (bestLen == Int.MAX_VALUE) {
            return ""
        }

        return s.substring(bestLeft, bestLeft + bestLen)
    }
}
