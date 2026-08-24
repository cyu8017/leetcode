// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

class Solution {
    func nextGreaterElement(_ n: Int) -> Int {
        var digits = Array(String(n))
        var i = digits.count - 2
        while i >= 0 && digits[i] >= digits[i + 1] {
            i -= 1
        }
        if i < 0 { return -1 }
        var j = digits.count - 1
        while digits[j] <= digits[i] {
            j -= 1
        }
        digits.swapAt(i, j)
        digits[(i + 1)...].reverse()
        let value = Int(String(digits)) ?? -1
        if value > Int32.max { return -1 }
        return value
    }
}
