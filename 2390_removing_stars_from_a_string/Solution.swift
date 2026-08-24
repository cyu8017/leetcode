// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

class Solution {
    func removeStars(_ s: String) -> String {
        var stack: [Character] = []
        for c in s {
            if c == "*" { stack.removeLast() }
            else { stack.append(c) }
        }
        return String(stack)
    }
}
