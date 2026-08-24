// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

class Solution {
    func firstMatchingIndex(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        for i in 0..<(n / 2 + 1) {
            if chars[i] == chars[n - i - 1] { return i }
        }
        return -1
    }
}
