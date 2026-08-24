// LeetCode 2325 - Decode the Message
// https://leetcode.com/problems/decode-the-message/

class Solution {
    func decodeMessage(_ key: String, _ message: String) -> String {
        var mp = [Character?](repeating: nil, count: 26)
        var next = Character("a").asciiValue!
        for c in key {
            if c == " " { continue }
            let i = Int(c.asciiValue! - 97)
            if mp[i] != nil { continue }
            mp[i] = Character(UnicodeScalar(Int(next))!)
            next += 1
        }
        return String(message.map { c in
            if c == " " { return c }
            return mp[Int(c.asciiValue! - 97)]!
        })
    }
}
