// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/


class Solution {
    func isAdjacentDiffAtMostTwo(_ s: String) -> Bool {
        let chars = Array(s)
        for i in 1..<chars.count {
            let a = Int(chars[i - 1].asciiValue!)
            let b = Int(chars[i].asciiValue!)
            if abs(a - b) > 2 { return false }
        }
        return true
    }
}
