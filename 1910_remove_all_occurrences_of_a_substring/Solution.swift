// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution {
    func removeOccurrences(_ s: String, _ part: String) -> String {
        let partChars = Array(part)
        let m = partChars.count
        var stack: [Character] = []
        for ch in s {
            stack.append(ch)
            if stack.count >= m && Array(stack.suffix(m)) == partChars {
                stack.removeLast(m)
            }
        }
        return String(stack)
    }
}
