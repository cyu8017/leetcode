// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution {
    func subtractProductAndSum(_ n: Int) -> Int {
        var n = n, prod = 1, sum = 0
        while n > 0 {
            let d = n % 10
            prod *= d
            sum += d
            n /= 10
        }
        return prod - sum
    }
}
