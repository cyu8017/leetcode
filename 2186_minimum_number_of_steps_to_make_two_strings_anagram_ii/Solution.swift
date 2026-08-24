// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution {
    func minSteps(_ s: String, _ t: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        for c in s { freq[Int(c.asciiValue! - 97)] += 1 }
        for c in t { freq[Int(c.asciiValue! - 97)] -= 1 }
        return freq.reduce(0) { $0 + abs($1) }
    }
}
