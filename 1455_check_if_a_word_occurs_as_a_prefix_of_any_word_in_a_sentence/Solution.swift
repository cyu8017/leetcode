// LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution {
    func isPrefixOfWord(_ sentence: String, _ searchWord: String) -> Int {
        for (i, w) in sentence.split(separator: " ").enumerated() {
            if w.hasPrefix(searchWord) { return i + 1 }
        }
        return -1
    }
}
