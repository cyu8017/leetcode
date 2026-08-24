// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution {
    private val rank = IntArray(26)

    fun isAlienSorted(words: Array<String>, order: String): Boolean {
        for (i in 0 until 26) rank[order[i] - 'a'] = i
        for (i in 0 until words.size - 1)
            if (!lessEq(words[i], words[i + 1])) return false
        return true
    }

    private fun lessEq(a: String, b: String): Boolean {
        val n = minOf(a.length, b.length)
        for (i in 0 until n) {
            if (rank[a[i] - 'a'] != rank[b[i] - 'a'])
                return rank[a[i] - 'a'] < rank[b[i] - 'a']
        }
        return a.length <= b.length
    }
}
