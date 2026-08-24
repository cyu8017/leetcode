// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

class Solution {
    fun minimumSteps(s: String): Long {
        var ans = 0
        var zeros = 0
        for (i in s.length - 1 downTo 0) {
            if (s[i] == '0') zeros++
            else ans += zeros
        }
        return ans
    }
}
