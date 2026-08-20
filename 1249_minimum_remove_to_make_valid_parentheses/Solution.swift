// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution {
    func minRemoveToMakeValid(_ s: String) -> String {
        var chars = Array(s)
        var stack: [Int] = []
        for i in 0..<chars.count {
            if chars[i] == "(" {
                stack.append(i)
            } else if chars[i] == ")" {
                if stack.isEmpty { chars[i] = "*" }
                else { stack.removeLast() }
            }
        }
        for i in stack { chars[i] = "*" }
        return String(chars.filter { $0 != "*" })
    }
}
