// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        var openNeed = 0, closeNeed = 0
        for ch in s {
            if ch == "(" { closeNeed += 1 }
            else if closeNeed > 0 { closeNeed -= 1 }
            else { openNeed += 1 }
        }
        return openNeed + closeNeed
    }
}
