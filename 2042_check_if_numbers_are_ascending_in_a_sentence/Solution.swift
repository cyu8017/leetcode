// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution {
    func areNumbersAscending(_ s: String) -> Bool {
        var prev = -1
        for tok in s.split(separator: " ") {
            if let v = Int(tok) {
                if v <= prev { return false }
                prev = v
            }
        }
        return true
    }
}
