// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

class Solution {
    func judgeSquareSum(_ c: Int) -> Bool {
        var left = 0
        var right = Int(Double(c).squareRoot())
        while left <= right {
            let total = left * left + right * right
            if total == c { return true }
            if total < c { left += 1 } else { right -= 1 }
        }
        return false
    }
}
