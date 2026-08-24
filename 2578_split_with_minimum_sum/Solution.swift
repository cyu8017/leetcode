// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

class Solution {
    func splitNum(_ num: Int) -> Int {
        var digits = [Int]()
        var num = num
        while num > 0 {
            digits.append(num % 10)
            num /= 10
        }
        digits.sort()
        var a = 0, b = 0
        for i in 0..<digits.count {
            if i % 2 == 0 { a = a * 10 + digits[i] }
            else { b = b * 10 + digits[i] }
        }
        return a + b
    }
}
