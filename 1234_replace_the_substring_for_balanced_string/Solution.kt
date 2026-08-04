// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution {
    fun balancedString(s: String): Int {
        val count = IntArray(128)
        for (ch in s) count[ch.code]++
        val limit = s.length / 4
        val n = s.length
        var left = 0
        var answer = n
        for (right in 0 until n) {
            count[s[right].code]--
            while (left < n && count['Q'.code] <= limit && count['W'.code] <= limit
                && count['E'.code] <= limit && count['R'.code] <= limit
            ) {
                answer = minOf(answer, right - left + 1)
                count[s[left].code]++
                left++
            }
        }
        return answer
    }
}
