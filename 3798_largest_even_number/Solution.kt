// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

class Solution {
    fun largestEven(s0: String): String {
        var s = s0
        while (s.isNotEmpty() && s[s.length - 1] == '1') {
            s = s.substring(0, s.length - 1)
        }
        return s
    }
}
