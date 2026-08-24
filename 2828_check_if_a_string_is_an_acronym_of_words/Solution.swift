// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution {
    func isAcronym(_ words: [String], _ s: String) -> Bool {
        let chars = Array(s)
        if words.count != chars.count { return false }
        for i in words.indices {
            guard let first = words[i].first, first == chars[i] else { return false }
        }
        return true
    }
}
