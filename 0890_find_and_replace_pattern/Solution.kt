// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

class Solution {
    fun findAndReplacePattern(words: Array<String>, pattern: String): List<String> {
        val target = normalize(pattern)
        val ans = mutableListOf<String>()
        for (w in words) {
            if (normalize(w).contentEquals(target)) ans.add(w)
        }
        return ans
    }

    private fun normalize(s: String): IntArray {
        val mapping = HashMap<Char, Int>()
        val out = IntArray(s.length)
        for (i in s.indices) {
            val ch = s[i]
            mapping.putIfAbsent(ch, mapping.size)
            out[i] = mapping[ch]!!
        }
        return out
    }
}
