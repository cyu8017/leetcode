// LeetCode 3754 - Concatenate Non Zero Digits And Multiply By Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution {
    fun sumAndMultiply(n: Int): Long {
        var p = 1
        var x = 0
        var s = 0
        while (n > 0) {
            var v = n % 10
            if (v != 0) {
                s += v
                x += p * v
                p *= 10
            }
            n /= 10
        }
        return 1L * x * s
    }
}
