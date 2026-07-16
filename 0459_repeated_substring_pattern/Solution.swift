// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

class Solution {
    func repeatedSubstringPattern(_ s: String) -> Bool {
        let doubled = s + s
        let start = doubled.index(doubled.startIndex, offsetBy: 1)
        let end = doubled.index(doubled.endIndex, offsetBy: -1)
        return doubled[start..<end].contains(s)
    }
}
