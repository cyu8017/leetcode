// LeetCode 0205 - Isomorphic Strings\n// https://leetcode.com/problems/\n\nclass Solution {
    fun isIsomorphic(s: String, t: String): Boolean {
        val forward = mutableMapOf<Char, Char>(); val backward = mutableMapOf<Char, Char>()
        for (i in s.indices) {
            val a = s[i]; val b = t[i]
            if ((forward[a] != null && forward[a] != b) || (backward[b] != null && backward[b] != a)) return false
            forward[a] = b; backward[b] = a
        }
        return true
    }
}
