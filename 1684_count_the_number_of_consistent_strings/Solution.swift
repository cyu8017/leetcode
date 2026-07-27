// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution {
    func countConsistentStrings(_ allowed: String, _ words: [String]) -> Int {
        let a = Set(allowed)
        return words.filter { w in w.allSatisfy { a.contains($0) } }.count
    }
}
