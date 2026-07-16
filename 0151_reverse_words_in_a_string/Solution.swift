// LeetCode 0151 - Reverse Words in a String
// https://leetcode.com/problems/reverse-words-in-a-string/

class Solution {
    func reverseWords(_ s: String) -> String {
        return s.split(whereSeparator: \.isWhitespace).reversed().joined(separator: " ")
    }
}