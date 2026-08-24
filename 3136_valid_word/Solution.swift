// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

class Solution {
    func isValid(_ word: String) -> Bool {
        if word.count < 3 { return false }
        var hasVowel = false, hasConsonant = false
        let vowels = Set("aeiouAEIOU")
        for c in word {
            if c.isLetter {
                if vowels.contains(c) { hasVowel = true }
                else { hasConsonant = true }
            } else if !c.isNumber {
                return false
            }
        }
        return hasVowel && hasConsonant
    }
}
