// LeetCode 1422 - Maximum Score After Splitting a String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution {
    fun maxScore(s: String): Int {
        var ones = s.count { it == '1' }
        var leftZeros = 0
        var answer = 0
        for (i in 0 until s.length - 1) {
            if (s[i] == '0') leftZeros++ else ones--
            answer = maxOf(answer, leftZeros + ones)
        }
        return answer
    }
}
