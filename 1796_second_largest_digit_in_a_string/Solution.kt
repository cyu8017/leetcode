// LeetCode 1796 - Second Largest Digit in a String
// https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution {
    fun secondHighest(s: String): Int {
        var largest = -1
        var second = -1
        for (ch in s) {
            if (ch.isDigit()) {
                val d = ch - '0'
                if (d > largest) {
                    second = largest
                    largest = d
                } else if (d < largest && d > second) {
                    second = d
                }
            }
        }
        return second
    }
}
