// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

class Solution {
    fun smallestBeautifulString(s: String, k: Int): String {
        val n = s.length
        val b = s.toCharArray()
        for (i in n - 1 downTo 0) {
            var c = (b[i].code + 1).toChar()
            while (c.code < 'a'.code + k) {
                if ((i > 0 && c == b[i - 1]) || (i > 1 && c == b[i - 2])) {
                    c = (c.code + 1).toChar()
                    continue
                }
                b[i] = c
                for (j in i + 1 until n) {
                    var nc = 'a'
                    while (nc.code < 'a'.code + k) {
                        if ((j > 0 && nc == b[j - 1]) || (j > 1 && nc == b[j - 2])) {
                            nc = (nc.code + 1).toChar()
                            continue
                        }
                        b[j] = nc
                        break
                    }
                }
                return String(b)
            }
        }
        return ""
    }
}
