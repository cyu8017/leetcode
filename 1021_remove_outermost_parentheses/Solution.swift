// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

class Solution {
    func removeOuterParentheses(_ s: String) -> String {
        var ans = [Character]()
        var depth = 0
        for ch in s {
            if ch == "(" {
                if depth > 0 { ans.append(ch) }
                depth += 1
            } else {
                depth -= 1
                if depth > 0 { ans.append(ch) }
            }
        }
        return String(ans)
    }
}
