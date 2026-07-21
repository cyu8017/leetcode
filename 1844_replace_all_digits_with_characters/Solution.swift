// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution {
    func replaceDigits(_ s: String) -> String {
        var chars = Array(s)
        var i = 1
        while i < chars.count {
            let shift = Int(String(chars[i]))!
            let base = chars[i - 1].asciiValue!
            chars[i] = Character(UnicodeScalar(base + UInt8(shift)))
            i += 2
        }
        return String(chars)
    }
}
