// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []
        let pairs: [Character: Character] = [")": "(", "]": "[", "}": "{"]

        for ch in s {
            if ch == "(" || ch == "[" || ch == "{" {
                stack.append(ch)
            } else if stack.isEmpty || stack.removeLast() != pairs[ch] {
                return false
            }
        }

        return stack.isEmpty
    }
}
