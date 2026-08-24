// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

class Solution {
    func decodeAtIndex(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        var size = 0
        for ch in chars {
            if ch.isNumber { size *= Int(String(ch))! }
            else { size += 1 }
        }
        var kk = k
        for ch in chars.reversed() {
            kk %= size
            if kk == 0 && ch.isLetter { return String(ch) }
            if ch.isNumber { size /= Int(String(ch))! }
            else { size -= 1 }
        }
        return ""
    }
}
