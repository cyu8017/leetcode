// LeetCode 3536 - Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution {
    func maxProduct(_ n: Int) -> Int {
        var n = n, a = 0, b = 0
        while n > 0 {
            let x = n % 10
            if a < x { b = a; a = x }
            else if b < x { b = x }
            n /= 10
        }
        return a * b
    }
}
