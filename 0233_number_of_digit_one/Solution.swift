// LeetCode 0233 - Number of Digit One
// https://leetcode.com/problems/number-of-digit-one/

class Solution {
    func countDigitOne(_ n: Int) -> Int {
        var count: Int64 = 0
        var factor: Int64 = 1
        var value = Int64(n)
        while factor <= value {
            let lower = value % factor
            let current = (value / factor) % 10
            let higher = value / (factor * 10)
            if current == 0 {
                count += higher * factor
            } else if current == 1 {
                count += higher * factor + lower + 1
            } else {
                count += (higher + 1) * factor
            }
            factor *= 10
        }
        return Int(count)
    }
}
