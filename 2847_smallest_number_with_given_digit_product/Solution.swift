// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

class Solution {
    func smallestNumber(_ n: Int) -> String {
        if n == 0 { return "0" }
        if n == 1 { return "1" }
        var n = n
        var digits: [Character] = []
        for d in stride(from: 9, through: 2, by: -1) {
            while n % d == 0 {
                digits.append(Character(String(d)))
                n /= d
            }
        }
        if n > 1 { return "-1" }
        return String(digits.reversed())
    }
}
