// LeetCode 1974
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution {
    fun minTimeToType(word: String): Int {
        var cur = 'a'
        var ans = 0
        for (ch in word) {
            val d = kotlin.math.abs(ch - cur)
            ans += minOf(d, 26 - d) + 1
            cur = ch
        }
        return ans
    }
}
