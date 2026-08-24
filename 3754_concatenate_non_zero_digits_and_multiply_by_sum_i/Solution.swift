// LeetCode 3754 - Concatenate Non Zero Digits And Multiply By Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution {
    func sumAndMultiply(_ n: Int) -> Int {
        var n = n
        var p = 1, x = 0, s = 0
        while n > 0 {
            let v = n % 10
            if v != 0 {
                s += v
                x += p * v
                p *= 10
            }
            n /= 10
        }
        return x * s
    }
}
