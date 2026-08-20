// LeetCode 1347 - Minimum Number of Steps to Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution {
    func minSteps(_ s: String, _ t: String) -> Int {
        var counts = Array(repeating: 0, count: 26)
        for ch in s.utf8 { counts[Int(ch) - 97] += 1 }
        for ch in t.utf8 { counts[Int(ch) - 97] -= 1 }
        return counts.filter { $0 > 0 }.reduce(0, +)
    }
}
