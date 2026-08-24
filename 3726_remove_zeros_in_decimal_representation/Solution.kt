// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

class Solution {
    fun removeZeros(n: Long): Long {
        var ans = 0
        var k = 1
        while (n > 0) {
            var x = n % 10
            if (x > 0) {
                ans = k * x + ans
                k *= 10
            }
            n /= 10
        }
        return ans
    }
}
