// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution {
    func areOccurrencesEqual(_ s: String) -> Bool {
        var freq: [Character: Int] = [:]
        for c in s { freq[c, default: 0] += 1 }
        return Set(freq.values).count == 1
    }
}
