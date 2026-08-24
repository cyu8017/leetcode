// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

class Solution {
    func backspaceCompare(_ s: String, _ t: String) -> Bool {
        return build(s) == build(t)
    }

    private func build(_ text: String) -> String {
        var stack = [Character]()
        for ch in text {
            if ch == "#" {
                if !stack.isEmpty { stack.removeLast() }
            } else {
                stack.append(ch)
            }
        }
        return String(stack)
    }
}
