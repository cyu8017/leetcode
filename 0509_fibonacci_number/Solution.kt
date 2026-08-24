// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

class Solution {
    fun fib(n: Int): Int {
        if (n <= 1) {
            return n
        }
        var previous = 0
        var current = 1
        for (index in 2..n) {
            val next = previous + current
            previous = current
            current = next
        }
        return current
    }
}
