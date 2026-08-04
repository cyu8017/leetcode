// LeetCode 1446 - Consecutive Characters
// https://leetcode.com/problems/consecutive-characters/

class Solution {
    fun maxPower(s: String): Int {
        var answer = 1
        var run = 1
        for (i in 1 until s.length) {
            run = if (s[i] == s[i - 1]) run + 1 else 1
            answer = maxOf(answer, run)
        }
        return answer
    }
}
