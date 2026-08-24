// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

class Solution {
    func scoreOfParentheses(_ s: String) -> Int {
        var stack = [0]
        for ch in s {
            if ch == "(" {
                stack.append(0)
            } else {
                let val = stack.removeLast()
                stack[stack.count - 1] += max(2 * val, 1)
            }
        }
        return stack[0]
    }
}
