// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution {
    func numDifferentIntegers(_ word: String) -> Int {
        var seen = Set<String>()
        var current = ""
        for ch in word {
            if ch.isNumber {
                current.append(ch)
            } else if !current.isEmpty {
                seen.insert(normalize(current))
                current = ""
            }
        }
        if !current.isEmpty {
            seen.insert(normalize(current))
        }
        return seen.count
    }

    private func normalize(_ s: String) -> String {
        var i = s.startIndex
        while i < s.endIndex && s[i] == "0" {
            i = s.index(after: i)
        }
        if i == s.endIndex { return "0" }
        return String(s[i...])
    }
}
