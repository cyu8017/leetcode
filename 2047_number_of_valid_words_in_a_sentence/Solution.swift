// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution {
    func countValidWords(_ sentence: String) -> Int {
        return sentence.split(separator: " ", omittingEmptySubsequences: false).filter { valid(String($0)) }.count
    }

    private func valid(_ w: String) -> Bool {
        if w.isEmpty { return false }
        let chars = Array(w)
        var hyphen = 0
        for i in 0..<chars.count {
            let c = chars[i]
            if c >= "0" && c <= "9" { return false }
            if c == "-" {
                hyphen += 1
                if hyphen > 1 || i == 0 || i == chars.count - 1 { return false }
                if chars[i - 1] < "a" || chars[i - 1] > "z" || chars[i + 1] < "a" || chars[i + 1] > "z" { return false }
            } else if c == "!" || c == "." || c == "," {
                if i != chars.count - 1 { return false }
            } else if c < "a" || c > "z" {
                return false
            }
        }
        return true
    }
}
