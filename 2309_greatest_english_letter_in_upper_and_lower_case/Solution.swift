// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution {
    func greatestLetter(_ s: String) -> String {
        var lower = [Bool](repeating: false, count: 26)
        var upper = [Bool](repeating: false, count: 26)
        for c in s {
            if c.isLowercase { lower[Int(c.asciiValue! - 97)] = true }
            else if c.isUppercase { upper[Int(c.asciiValue! - 65)] = true }
        }
        for i in stride(from: 25, through: 0, by: -1) {
            if lower[i] && upper[i] { return String(Character(UnicodeScalar(65 + i)!)) }
        }
        return ""
    }
}
