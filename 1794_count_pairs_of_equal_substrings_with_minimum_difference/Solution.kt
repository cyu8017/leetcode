// LeetCode 1794 - Count Pairs of Equal Substrings With Minimum Difference
// https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/

class Solution {
    fun countQuadruples(firstString: String, secondString: String): Long {
        val first = IntArray(26) { -1 }
        val lastF = IntArray(26) { -1 }
        val lastS = IntArray(26) { -1 }
        for (i in firstString.indices) {
            val c = firstString[i] - 'a'
            if (first[c] == -1) first[c] = i
            lastF[c] = i
        }
        for (i in secondString.indices) {
            lastS[secondString[i] - 'a'] = i
        }
        var best = Long.MAX_VALUE
        for (c in 0 until 26) {
            if (first[c] != -1 && lastS[c] != -1) {
                best = minOf(best, (lastF[c] - lastS[c]).toLong())
            }
        }
        if (best == Long.MAX_VALUE) return 0
        var ans = 0L
        for (c in 0 until 26) {
            if (first[c] == -1 || lastS[c] == -1 || (lastF[c] - lastS[c]).toLong() != best) continue
            var iCount = 0L
            for (k in first[c]..lastF[c]) {
                if (firstString[k] - 'a' == c) iCount++
            }
            var aCount = 0L
            for (k in 0..lastS[c]) {
                if (secondString[k] - 'a' == c) aCount++
            }
            ans += iCount * aCount
        }
        return ans
    }
}
