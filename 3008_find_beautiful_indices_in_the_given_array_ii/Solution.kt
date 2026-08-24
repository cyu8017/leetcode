// LeetCode 3008 - Find Beautiful Indices in the Given Array II
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/

class Solution {
    private fun buildLPS(lps: IntArray, pattern: String) {
        var l = 0
        var i = 1
        val sL = pattern.length
        lps[0] = 0
        while (i < sL) {
            if (pattern[i] == pattern[l]) {
                l++
                lps[i] = l
                i++
            } else if (l != 0) {
                l = lps[l - 1]
            } else {
                lps[i] = l
                i++
            }
        }
    }

    private fun kmp(s: String, pat: String, lps: IntArray, index: MutableList<Int>) {
        val sLen = s.length
        val patL = pat.length
        var i = 0
        var j = 0
        while (sLen - i >= patL - j) {
            if (s[i] == pat[j]) {
                i++
                j++
            }
            if (j == patL) {
                index.add(i - patL)
                j = lps[j - 1]
            } else if (i < sLen && s[i] != pat[j]) {
                if (j != 0) j = lps[j - 1]
                else i++
            }
        }
    }

    fun beautifulIndices(s: String, a: String, b: String, k: Int): MutableList<Int> {
        val lpsA = IntArray(a.length)
        val lpsB = IntArray(b.length)
        val aIndex = ArrayList<Int>()
        val bIndex = ArrayList<Int>()
        val result = ArrayList<Int>()
        buildLPS(lpsA, a)
        buildLPS(lpsB, b)
        kmp(s, a, lpsA, aIndex)
        kmp(s, b, lpsB, bIndex)
        var i = 0
        var j = 0
        while (i < aIndex.size && j < bIndex.size) {
            if (aIndex[i] + k >= bIndex[j] && aIndex[i] - k <= bIndex[j]) {
                result.add(aIndex[i])
                i++
            } else if (aIndex[i] - k > bIndex[j]) {
                j++
            } else {
                i++
            }
        }
        return result
    }
}
