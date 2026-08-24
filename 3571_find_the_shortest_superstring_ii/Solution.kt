// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

class Solution {
    fun shortestSuperstring(s1: String, s2: String): String {
        if (s1.length > s2.length) return shortestSuperstring(s2, s1)
        var m = s1.length
        if (s2.contains(s1)) return s2
        for (i in 0 until m) {
            if (s2.startsWith(s1.substring(i))) return s1.substring(0, i) + s2
            var len = m - i
            if (s2.length() >= len && s2.substring(s2.length() - len) == s1.substring(0, len))
                return s2 + s1.substring(m - i)
        }
        return s1 + s2
    }
}
