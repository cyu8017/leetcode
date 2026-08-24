
// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

class Solution {
    fun fibGenerator(): () -> Int {
        var a = 0
        var b = 1
        return {
            val v = a
            val na = b
            b = a + b
            a = na
            v
        }
    }
}
