// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution {
    fun shortestToChar(s: String, c: Char): IntArray {
        var n = s.length
        var ans = IntArray(n)
        var prev = -n
        for (i in 0 until n) {
            if (s[i] == c) prev = i
            ans[i] = i - prev
        }
        prev = 2 * n
        for (i in n - 1 downTo 0) {
            if (s[i] == c) prev = i
            ans[i] = minOf(ans[i], prev - i)
        }
        return ans
    }
}
