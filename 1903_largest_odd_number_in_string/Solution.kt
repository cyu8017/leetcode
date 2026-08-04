// LeetCode 1903 - Largest Odd Number In String
// https://leetcode.com/problems/largest-odd-number-in-string/

class Solution {
    fun largestOddNumber(num: String): String {
        for (i in num.indices.reversed()) {
            if ((num[i] - '0') % 2 == 1) return num.substring(0, i + 1)
        }
        return ""
    }
}
