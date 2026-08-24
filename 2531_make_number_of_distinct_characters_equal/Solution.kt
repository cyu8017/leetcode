// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

class Solution {
    fun isItPossible(word1: String, word2: String): Boolean {
        val c1 = IntArray(26)
        val c2 = IntArray(26)
        for (c in word1) c1[c - 'a'] += 1
        for (c in word2) c2[c - 'a'] += 1
        var d1 = 0
        var d2 = 0
        for (i in 0 until 26) {
            if (c1[i] > 0) d1 += 1
            if (c2[i] > 0) d2 += 1
        }
        for (a in 0 until 26) {
            if (c1[a] == 0) continue
            for (b in 0 until 26) {
                if (c2[b] == 0) continue
                var nd1 = d1
                var nd2 = d2
                if (a == b) {
                    if (nd1 == nd2) return true
                    continue
                }
                if (c1[a] == 1) nd1 -= 1
                if (c1[b] == 0) nd1 += 1
                if (c2[b] == 1) nd2 -= 1
                if (c2[a] == 0) nd2 += 1
                if (nd1 == nd2) return true
            }
        }
        return false
    }
}
