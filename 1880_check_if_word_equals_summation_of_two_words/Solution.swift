// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution {
    func isSumEqual(_ firstWord: String, _ secondWord: String, _ targetWord: String) -> Bool {
        return wordValue(firstWord) + wordValue(secondWord) == wordValue(targetWord)
    }

    private func wordValue(_ word: String) -> Int {
        var digits = ""
        for ch in word {
            digits += String(Int(ch.asciiValue! - Character("a").asciiValue!))
        }
        return Int(digits) ?? 0
    }
}
