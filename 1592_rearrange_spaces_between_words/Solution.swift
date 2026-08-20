// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution {
    func reorderSpaces(_ text: String) -> String {
        let words = text.split(whereSeparator: { $0 == " " }).map(String.init)
        let spaces = text.filter { $0 == " " }.count
        if words.count == 1 { return words[0] + String(repeating: " ", count: spaces) }
        let between = spaces / (words.count - 1)
        let trailing = spaces % (words.count - 1)
        return words.joined(separator: String(repeating: " ", count: between)) + String(repeating: " ", count: trailing)
    }
}
