// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution {
    func numOfStrings(_ patterns: [String], _ word: String) -> Int {
        patterns.filter { word.contains($0) }.count
    }
}
