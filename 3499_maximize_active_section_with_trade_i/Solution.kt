// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

class Solution {
    fun maxActiveSectionsAfterTrade(s: String): Int {
        var ones = 0
        for (c in s.toCharArray()) { if (c == '1') ones++ }
        var zeros = ArrayList<IntArray>()
        var n = s.length
        var i = 0
        while (i < n) {
            if (s[i] != '0') { i++; continue; }
            var j = i
            while (j < n && s[j] == '0') j++
            zeros.add(intArrayOf(i, j - 1))
            i = j
            
        }
        var best = 0
        var i = 0
        while (i + 1 < zeros.size) {
            var gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1)
            if (gain > best) best = gain
            i = i + 1
        }
        return ones + best
    }
}
