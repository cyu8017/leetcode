// LeetCode 1404 - Number of Steps to Reduce a Number in Binary Representation to One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution {
    fun numSteps(s: String): Int {
        var steps = 0
        var carry = 0
        for (i in s.length - 1 downTo 1) {
            val value = (s[i] - '0') + carry
            if (value == 1) {
                steps += 2
                carry = 1
            } else {
                steps += 1
            }
        }
        return steps + carry
    }
}
