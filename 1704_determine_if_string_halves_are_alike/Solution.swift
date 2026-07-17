// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution {
    func halvesAreAlike(_ s: String) -> Bool {
        let vowels = Set("aeiouAEIOU")
        let chars = Array(s)
        let mid = chars.count / 2
        var balance = 0
        for (i, ch) in chars.enumerated() {
            if vowels.contains(ch) {
                balance += i < mid ? 1 : -1
            }
        }
        return balance == 0
    }
}
