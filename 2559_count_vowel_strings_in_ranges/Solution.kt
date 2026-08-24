// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution {
    fun vowelStrings(words: Array<String>, queries: Array<IntArray>): IntArray {
        val n = words.size
        val pref = IntArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i]
            val w = words[i]
            if (w.isNotEmpty() && isV(w[0]) && isV(w[w.length - 1])) pref[i + 1] += 1
        }
        return IntArray(queries.size) { i -> pref[queries[i][1] + 1] - pref[queries[i][0]] }
    }

    private fun isV(c: Char): Boolean =
        c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
