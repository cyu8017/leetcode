// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

class Solution {
    func smallestFactorization(_ num: Int) -> Int {
        if num < 10 { return num }
        var num = num
        var digits = [Int]()
        for digit in stride(from: 9, through: 2, by: -1) {
            while num % digit == 0 {
                digits.append(digit)
                num /= digit
            }
        }
        if num != 1 { return 0 }
        var result = 0
        for d in digits.reversed() {
            result = result * 10 + d
            if result > Int32.max { return 0 }
        }
        return result
    }
}
