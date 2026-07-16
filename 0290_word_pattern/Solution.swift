// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

class Solution {
    func wordPattern(_ pattern: String, _ s: String) -> Bool {
        let words = s.split(separator: " ").map(String.init)
        if pattern.count != words.count {
            return false
        }
        var charToWord: [Character: String] = [:]
        var wordToChar: [String: Character] = [:]
        let chars = Array(pattern)
        for index in 0..<chars.count {
            let char = chars[index]
            let word = words[index]
            if let mapped = charToWord[char] {
                if mapped != word {
                    return false
                }
            } else if wordToChar[word] != nil {
                return false
            } else {
                charToWord[char] = word
                wordToChar[word] = char
            }
        }
        return true
    }
}
