// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

class Solution {
    func longestValidParentheses(_ s: String) -> Int {
        var stack = [-1]
        var best = 0
        let chars = Array(s)

        for i in chars.indices {
            if chars[i] == "(" {
                stack.append(i)
            } else {
                stack.removeLast()
                if stack.isEmpty {
                    stack.append(i)
                } else {
                    best = max(best, i - stack.last!)
                }
            }
        }

        return best
    }
}
