// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution {
    func prefixCount(_ words: [String], _ pref: String) -> Int {
        words.filter { $0.hasPrefix(pref) }.count
    }
}
