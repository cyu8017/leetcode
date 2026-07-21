// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

class Solution {
    func sortSentence(_ s: String) -> String {
        let tokens = s.split(separator: " ")
        var ordered = Array(repeating: "", count: tokens.count)

        for token in tokens {
            let position = Int(token.last!)! - 1
            ordered[position] = String(token.dropLast())
        }

        return ordered.joined(separator: " ")
    }
}
