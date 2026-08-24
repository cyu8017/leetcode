// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution {
    func isSubstringPresent(_ s: String) -> Bool {
        let chars = Array(s)
        var st = Array(repeating: Array(repeating: false, count: 26), count: 26)
        let a = Character("a").asciiValue!
        if chars.count >= 2 {
            for i in 0..<(chars.count - 1) {
                st[Int(chars[i + 1].asciiValue! - a)][Int(chars[i].asciiValue! - a)] = true
            }
            for i in 0..<(chars.count - 1) {
                if st[Int(chars[i].asciiValue! - a)][Int(chars[i + 1].asciiValue! - a)] { return true }
            }
        }
        return false
    }
}
