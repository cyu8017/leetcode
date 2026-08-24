// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution {
    fun maximumValue(strs: Array<String>): Int {
        var ans = 0
        for (s in strs) {
            var allDigit = true
            var value = 0
            for (c in s) {
                if (c < '0' || c > '9') {
                    allDigit = false
                    break
                }
                value = value * 10 + (c - '0')
            }
            if (!allDigit) value = s.length
            if (value > ans) ans = value
        }
        return ans
    }
}
