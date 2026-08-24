// LeetCode 0600 - Non-negative Integers without Consecutive Ones
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/


class Solution {
    fun findIntegers(n: Int): Int {
        val fib = IntArray(32)
        fib[0] = 1
        fib[1] = 2
        for (i in 2 until 32) fib[i] = fib[i - 1] + fib[i - 2]
        var result = 0
        var prevBit = 0
        for (k in 30 downTo 0) {
            if ((n and (1 shl k)) != 0) {
                result += fib[k]
                if (prevBit == 1) return result
                prevBit = 1
            } else {
                prevBit = 0
            }
        }
        return result + 1
    }
}
