// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

class Solution {
    func splitWordsBySeparator(_ words: [String], _ separator: Character) -> [String] {
        var ans: [String] = []
        for w in words {
            let chars = Array(w)
            var start = 0
            for i in 0...chars.count {
                if i == chars.count || chars[i] == separator {
                    if i > start { ans.append(String(chars[start..<i])) }
                    start = i + 1
                }
            }
        }
        return ans
    }
}
