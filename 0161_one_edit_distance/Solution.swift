// LeetCode 0161 - One Edit Distance
// https://leetcode.com/problems/one-edit-distance/

class Solution {
    func isOneEditDistance(_ s: String, _ t: String) -> Bool {
        let sChars = Array(s)
        let tChars = Array(t)
        if abs(sChars.count - tChars.count) > 1 || s == t { return false }
        let (shorter, longer) = sChars.count <= tChars.count ? (sChars, tChars) : (tChars, sChars)
        var index = 0
        while index < shorter.count && shorter[index] == longer[index] { index += 1 }
        return shorter.count == longer.count
            ? Array(shorter.dropFirst(index + 1)) == Array(longer.dropFirst(index + 1))
            : Array(shorter.dropFirst(index)) == Array(longer.dropFirst(index + 1))
    }
}