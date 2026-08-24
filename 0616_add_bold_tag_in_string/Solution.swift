// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

class Solution {
    func addBoldTag(_ s: String, _ words: [String]) -> String {
        let chars = Array(s)
        let n = chars.count
        var bold = Array(repeating: false, count: n)
        for word in words {
            var searchStart = s.startIndex
            while let range = s.range(of: word, range: searchStart..<s.endIndex) {
                let start = s.distance(from: s.startIndex, to: range.lowerBound)
                for i in start..<(start + word.count) { bold[i] = true }
                searchStart = s.index(after: range.lowerBound)
            }
        }
        var parts = ""
        var i = 0
        while i < n {
            if bold[i] {
                parts += "<b>"
                while i < n && bold[i] {
                    parts.append(chars[i])
                    i += 1
                }
                parts += "</b>"
            } else {
                parts.append(chars[i])
                i += 1
            }
        }
        return parts
    }
}
