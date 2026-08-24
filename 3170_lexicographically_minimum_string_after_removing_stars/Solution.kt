// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

class Solution {
    fun clearStars(s: String): String {
        @SuppressWarnings("unchecked")
        List<Int>[] g = ArrayList[26]
        for (i in 0 until 26) { g[i] = ArrayList() }
        var n = s.length
        var rem = BooleanArray(n)
        for (i in 0 until n) {
            if (s[i] == '*') {
                rem[i] = true
                for (j in 0 until 26) {
                    if (!g[j].isEmpty()) {
                        rem[g[j][g[j].size - 1]] = true
                        g[j].remove(g[j].size - 1)
                        break
                    }
                }
            } else {
                g[s[i] - 'a'].add(i)
            }
        }
        var ans = StringBuilder()
        for (i in 0 until n) { if (!rem[i]) ans.append(s[i]) }
        return ans.toString()
    }
}
