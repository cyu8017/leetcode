// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

class Solution {
    func clearDigits(_ s: String) -> String {
        var stk: [Character] = []
        for c in s {
            if c.isNumber { stk.removeLast() }
            else { stk.append(c) }
        }
        return String(stk)
    }
}
