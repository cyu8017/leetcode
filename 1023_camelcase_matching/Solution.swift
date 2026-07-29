// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

class Solution {
    func camelMatch(_ queries: [String], _ pattern: String) -> [Bool] {
        let pattern = Array(pattern)
        func matches(_ q: String) -> Bool {
            var i = 0
            for ch in q {
                if i < pattern.count && ch == pattern[i] {
                    i += 1
                } else if ch.isUppercase {
                    return false
                }
            }
            return i == pattern.count
        }
        return queries.map { matches($0) }
    }
}
