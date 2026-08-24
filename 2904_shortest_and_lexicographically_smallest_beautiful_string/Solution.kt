// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution {
    fun shortestBeautifulSubstring(s: String, k: Int): String {
        var ans = ""
        val n = s.length
        for (i in 0 until n) {
            var ones = 0
            for (j in i until n) {
                if (s[j] == '1') ones++
                if (ones == k) {
                    val cand = s.substring(i, j + 1)
                    if (ans.isEmpty() || cand.length < ans.length || (cand.length == ans.length && cand < ans)) {
                        ans = cand
                    }
                    break
                }
                if (ones > k) break
            }
        }
        return ans
    }
}
