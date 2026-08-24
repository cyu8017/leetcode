// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

class Solution {
    fun generateString(str1: String, str2: String): String {
        val n = str1.length
        val m = str2.length
        val L = n + m - 1
        val ans = CharArray(L) { '?' }
        for (i in 0 until n) {
            if (str1[i] == 'T') {
                for (j in 0 until m) {
                    if (ans[i + j] != '?' && ans[i + j] != str2[j]) return ""
                    ans[i + j] = str2[j]
                }
            }
        }
        for (i in 0 until L) if (ans[i] == '?') ans[i] = 'a'
        for (i in 0 until n) {
            if (str1[i] == 'F') {
                var match = true
                for (j in 0 until m) if (ans[i + j] != str2[j]) { match = false; break }
                if (match) {
                    var changed = false
                    for (j in m - 1 downTo 0) {
                        val pos = i + j
                        var forced = false
                        for (t in 0 until n) {
                            if (str1[t] == 'T' && pos >= t && pos < t + m) { forced = true; break }
                        }
                        if (!forced) {
                            ans[pos] = 'b'
                            changed = true
                            break
                        }
                    }
                    if (!changed) return ""
                }
            }
        }
        for (i in 0 until n) {
            var match = true
            for (j in 0 until m) if (ans[i + j] != str2[j]) { match = false; break }
            if (str1[i] == 'T' && !match) return ""
            if (str1[i] == 'F' && match) return ""
        }
        return String(ans)
    }
}
