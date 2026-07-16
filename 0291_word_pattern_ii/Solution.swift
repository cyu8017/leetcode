// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

class Solution {
    func wordPatternMatch(_ pattern: String, _ s: String) -> Bool {
        let patternChars = Array(pattern)
        let stringChars = Array(s)
        var charToWord: [Character: String] = [:]
        var wordToChar: [String: Character] = [:]

        func backtrack(_ patternIndex: Int, _ stringIndex: Int) -> Bool {
            if patternIndex == patternChars.count {
                return stringIndex == stringChars.count
            }
            let char = patternChars[patternIndex]
            if let word = charToWord[char] {
                let wordChars = Array(word)
                guard stringIndex + wordChars.count <= stringChars.count else {
                    return false
                }
                for offset in 0..<wordChars.count {
                    if stringChars[stringIndex + offset] != wordChars[offset] {
                        return false
                    }
                }
                return backtrack(patternIndex + 1, stringIndex + wordChars.count)
            }
            for end in (stringIndex + 1)...stringChars.count {
                let word = String(stringChars[stringIndex..<end])
                if wordToChar[word] != nil {
                    continue
                }
                charToWord[char] = word
                wordToChar[word] = char
                if backtrack(patternIndex + 1, end) {
                    return true
                }
                charToWord.removeValue(forKey: char)
                wordToChar.removeValue(forKey: word)
            }
            return false
        }

        return backtrack(0, 0)
    }
}
