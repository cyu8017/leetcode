// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

class Solution {
    fun maximumOddBinaryNumber(s: String): String {
        var ones = 0
        for (i in 0 until s.length) { if (s[i] == '1') ones++ }
        var zeros = s.length - ones
        var b = StringBuilder(s.length)
        for (i in 0 until ones - 1) { b.append('1') }
        for (i in 0 until zeros) { b.append('0') }
        b.append('1')
        return b.toString()
    }
}
