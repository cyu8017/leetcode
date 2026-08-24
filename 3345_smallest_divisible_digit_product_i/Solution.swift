// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution {
    func smallestNumber(_ n: Int, _ t: Int) -> Int {
        var x = n
        while true {
            var p = 1, y = x
            while y > 0 { p *= y % 10; y /= 10 }
            if p % t == 0 { return x }
            x += 1
        }
    }
}
