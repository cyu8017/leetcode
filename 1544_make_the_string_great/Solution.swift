// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

class Solution {
    func makeGood(_ s: String) -> String {
        var stack = [Character]()
        for ch in s {
            if let last = stack.last,
               last != ch,
               String(last).lowercased() == String(ch).lowercased() {
                stack.removeLast()
            } else {
                stack.append(ch)
            }
        }
        return String(stack)
    }
}
