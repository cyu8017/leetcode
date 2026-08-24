// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

class Solution {
    func stringHash(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        let a = Character("a").asciiValue!
        var out = ""
        var i = 0
        while i < chars.count {
            var sum = 0
            for j in i..<(i + k) { sum += Int(chars[j].asciiValue! - a) }
            out.append(Character(UnicodeScalar(a + UInt8(sum % 26))))
            i += k
        }
        return out
    }
}
