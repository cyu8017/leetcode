// LeetCode 1451 - Rearrange Words in a Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution {
    func arrangeWords(_ text: String) -> String {
        var words = text.lowercased().split(separator: " ").map(String.init)
        words.sort { $0.count < $1.count }
        let joined = words.joined(separator: " ")
        guard let first = joined.first else { return "" }
        return String(first).uppercased() + joined.dropFirst()
    }
}
