// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

class Solution {
    func subStrHash(_ s: String, _ power: Int, _ modulo: Int, _ k: Int, _ hashValue: Int) -> String {
        let chars = Array(s)
        let n = chars.count
        var pk = 1
        for _ in 0..<(k - 1) { pk = pk * power % modulo }
        var h = 0
        var ans = 0
        for i in stride(from: n - 1, through: n - k, by: -1) {
            h = (h * power + Int(chars[i].asciiValue! - 96)) % modulo
        }
        if h == hashValue { ans = n - k }
        for i in stride(from: n - k - 1, through: 0, by: -1) {
            h = (h - Int(chars[i + k].asciiValue! - 96) * pk % modulo + modulo) % modulo
            h = (h * power + Int(chars[i].asciiValue! - 96)) % modulo
            if h == hashValue { ans = i }
        }
        return String(chars[ans..<(ans + k)])
    }
}
