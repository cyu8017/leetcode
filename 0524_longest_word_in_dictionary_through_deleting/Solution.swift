// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution {
    func findLongestWord(_ s: String, _ dictionary: [String]) -> String {
        var best = ""
        for word in dictionary {
            guard isSubsequence(s, word) else { continue }
            if word.count > best.count || (word.count == best.count && word < best) {
                best = word
            }
        }
        return best
    }

    private func isSubsequence(_ source: String, _ word: String) -> Bool {
        var index = word.startIndex
        for char in source {
            if index < word.endIndex && word[index] == char {
                index = word.index(after: index)
            }
        }
        return index == word.endIndex
    }
}
