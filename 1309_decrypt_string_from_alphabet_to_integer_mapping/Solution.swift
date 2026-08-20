// LeetCode 1309 - Decrypt String from Alphabet to Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution {
    func freqAlphabets(_ s: String) -> String {
        let chars = Array(s)
        var answer = [Character]()
        var i = chars.count - 1
        while i >= 0 {
            if chars[i] == "#" {
                let num = Int(String(chars[(i - 2)..<i]))!
                answer.append(Character(UnicodeScalar(96 + num)!))
                i -= 3
            } else {
                answer.append(Character(UnicodeScalar(96 + Int(String(chars[i]))!)!))
                i -= 1
            }
        }
        return String(answer.reversed())
    }
}
