// LeetCode 0205 - Isomorphic Strings
// https://leetcode.com/problems/isomorphic-strings/

class Solution {
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        let sChars = Array(s)
        let tChars = Array(t)
        guard sChars.count == tChars.count else { return false }
        var forward = [Character: Character]()
        var backward = [Character: Character]()
        for (a, b) in zip(sChars, tChars) {
            if let mapped = forward[a], mapped != b { return false }
            if let mapped = backward[b], mapped != a { return false }
            forward[a] = b
            backward[b] = a
        }
        return true
    }
}