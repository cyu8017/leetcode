// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution {
    fun reverseDegree(s: String): Int {
        var ans = 0
        for (i in 0 until s.length) {
            ans += (26 - (s[i] - 'a')) * (i + 1)
        }
        return ans
    }
}
