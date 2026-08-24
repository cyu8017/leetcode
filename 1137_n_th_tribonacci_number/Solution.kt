// LeetCode 1137 - N-th Tribonacci Number
// https://leetcode.com/problems/n-th-tribonacci-number/

class Solution {
    fun tribonacci(n: Int): Int {
        if (n == 0) return 0
        if (n <= 2) return 1
        var a = 0
        var b = 1
        var c = 1
        for (i in 3..n) {
            val next = a + b + c
            a = b
            b = c
            c = next
        }
        return c
    }
}
