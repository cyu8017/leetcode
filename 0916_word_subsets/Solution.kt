// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

class Solution {
    fun wordSubsets(words1: Array<String>, words2: Array<String>): List<String> {
        val need = IntArray(26)
        for (w in words2) {
            val cnt = IntArray(26)
            for (c in w) cnt[c - 'a']++
            for (i in 0 until 26) need[i] = maxOf(need[i], cnt[i])
        }
        val ans = mutableListOf<String>()
        for (w in words1) {
            val cnt = IntArray(26)
            for (c in w) cnt[c - 'a']++
            var ok = true
            for (i in 0 until 26) if (cnt[i] < need[i]) { ok = false; break }
            if (ok) ans.add(w)
        }
        return ans
    }
}
