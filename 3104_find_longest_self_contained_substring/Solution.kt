// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

class Solution {
    fun maxSubstringLength(s: String): Int {
        var first = IntArray(26), last = IntArray(26)
        for (i in 0 until 26) { first[i] = -1 }
        var n = s.length
        for (i in 0 until n) {
            var j = s[i] - 'a'
            if (first[j] == -1) first[j] = i
            last[j] = i
        }
        var ans = -1
        for (k in 0 until 26) {
            var i = first[k]
            if (i == -1) continue
            var mx = last[k]
            for (j in i until n) {
                var a = first[s[j] - 'a'], b = last[s[j] - 'a']
                if (a < i) break
                mx = maxOf(mx, b)
                if (mx == j && j - i + 1 < n) ans = maxOf(ans, j - i + 1)
            }
        }
        return ans
    }
}
