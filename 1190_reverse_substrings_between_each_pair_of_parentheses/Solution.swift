// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution {
    func reverseParentheses(_ s: String) -> String {
        var stack: [Character] = []
        for ch in s {
            if ch == ")" {
                var chunk: [Character] = []
                while let last = stack.last, last != "(" {
                    chunk.append(stack.removeLast())
                }
                _ = stack.popLast()
                stack.append(contentsOf: chunk)
            } else {
                stack.append(ch)
            }
        }
        return String(stack)
    }
}
