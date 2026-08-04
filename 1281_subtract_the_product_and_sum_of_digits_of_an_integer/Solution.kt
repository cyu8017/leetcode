// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution {
    fun subtractProductAndSum(n: Int): Int {
        var num = n
        var product = 1
        var total = 0
        while (num > 0) {
            val digit = num % 10
            product *= digit
            total += digit
            num /= 10
        }
        return product - total
    }
}
