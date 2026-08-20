// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution {
    func minSwaps(_ s: String) -> Int {
        var bal = 0, mx = 0
        for ch in s {
            if ch == "[" { bal += 1 } else { bal -= 1 }
            mx = min(mx, bal)
        }
        return (-mx + 1) / 2
    }
}
