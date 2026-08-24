// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution {
    fun checkDivisibility(n: Int): Boolean {
        var s = 0
        var p = 1
        var x = n
        while (x != 0) {
            var v = x % 10
            x /= 10
            s += v
            p *= v
        }
        return n % (s + p) == 0
    }
}
