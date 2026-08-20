// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution {
    func balancedStringSplit(_ s: String) -> Int {
        var bal = 0, ans = 0
        for ch in s {
            bal += ch == "L" ? 1 : -1
            if bal == 0 { ans += 1 }
        }
        return ans
    }
}
