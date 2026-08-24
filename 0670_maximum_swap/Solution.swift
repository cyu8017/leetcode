// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

class Solution {
    func maximumSwap(_ num: Int) -> Int {
        var digits = Array(String(num))
        var last = Array(repeating: -1, count: 10)
        for i in 0..<digits.count {
            last[Int(String(digits[i]))!] = i
        }
        for i in 0..<digits.count {
            let d = Int(String(digits[i]))!
            if d + 1 <= 9 {
                for candidate in stride(from: 9, through: d + 1, by: -1) {
                    if last[candidate] > i {
                        digits.swapAt(i, last[candidate])
                        return Int(String(digits))!
                    }
                }
            }
        }
        return num
    }
}
