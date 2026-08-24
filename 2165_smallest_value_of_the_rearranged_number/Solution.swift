// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

class Solution {
    func smallestNumber(_ num: Int) -> Int {
        var num = num
        let neg = num < 0
        if neg { num = -num }
        if num == 0 { return 0 }
        var digits = [Int]()
        while num > 0 { digits.append(num % 10); num /= 10 }
        if neg {
            digits.sort(by: >)
            var ans = 0
            for d in digits { ans = ans * 10 + d }
            return -ans
        }
        digits.sort()
        if digits[0] == 0 {
            for i in 1..<digits.count where digits[i] != 0 {
                digits.swapAt(0, i)
                break
            }
        }
        var res = 0
        for d in digits { res = res * 10 + d }
        return res
    }
}
