// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution {
    func removeDuplicates(_ s: String) -> String {
        var stack = [Character]()
        for ch in s {
            if let last = stack.last, last == ch {
                stack.removeLast()
            } else {
                stack.append(ch)
            }
        }
        return String(stack)
    }
}
