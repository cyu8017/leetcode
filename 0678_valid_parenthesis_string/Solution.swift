// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

class Solution {
    func checkValidString(_ s: String) -> Bool {
        var lo = 0, hi = 0
        for ch in s {
            if ch == "(" {
                lo += 1
                hi += 1
            } else if ch == ")" {
                lo = max(lo - 1, 0)
                hi -= 1
                if hi < 0 { return false }
            } else {
                lo = max(lo - 1, 0)
                hi += 1
            }
        }
        return lo == 0
    }
}
