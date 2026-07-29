// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution {
    func isValid(_ s: String) -> Bool {
        var stack = [Character]()
        for ch in s {
            stack.append(ch)
            if stack.count >= 3 {
                let n = stack.count
                if stack[n - 3] == "a" && stack[n - 2] == "b" && stack[n - 1] == "c" {
                    stack.removeLast(3)
                }
            }
        }
        return stack.isEmpty
    }
}
