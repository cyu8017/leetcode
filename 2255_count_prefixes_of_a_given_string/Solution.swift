// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution {
    func countPrefixes(_ words: [String], _ s: String) -> Int {
        words.filter { $0.count <= s.count && s.hasPrefix($0) }.count
    }
}
