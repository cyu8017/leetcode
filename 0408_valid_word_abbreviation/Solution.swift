// LeetCode 0408 - Valid Word Abbreviation
// https://leetcode.com/problems/valid-word-abbreviation/

class Solution {
    func validWordAbbreviation(_ word: String, _ abbr: String) -> Bool {
        let wordChars = Array(word)
        let abbrChars = Array(abbr)
        var i = 0
        var j = 0

        while i < wordChars.count && j < abbrChars.count {
            let abbrChar = abbrChars[j]
            if abbrChar.isNumber {
                if abbrChar == "0" {
                    return false
                }
                var number = 0
                while j < abbrChars.count, abbrChars[j].isNumber {
                    number = number * 10 + Int(String(abbrChars[j]))!
                    j += 1
                }
                i += number
            } else {
                if wordChars[i] != abbrChar {
                    return false
                }
                i += 1
                j += 1
            }
        }

        return i == wordChars.count && j == abbrChars.count
    }
}
