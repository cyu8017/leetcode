// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

class Solution {
    fun scoreOfString(s: String): Int {
        var ans = 0
        for (i in 1 until s.length) {
            ans += kotlin.math.abs(s[i - 1] - s[i])
        }
        return ans
    }
}
