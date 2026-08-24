// LeetCode 2116 - Check if a Parentheses String Can Be Valid
// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution {
    func canBeValid(_ s: String, _ locked: String) -> Bool {
        let sc = Array(s), lc = Array(locked)
        let n = sc.count
        if n % 2 != 0 { return false }
        var bal = 0
        for i in 0..<n {
            if lc[i] == "0" || sc[i] == "(" { bal += 1 }
            else { bal -= 1 }
            if bal < 0 { return false }
        }
        bal = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            if lc[i] == "0" || sc[i] == ")" { bal += 1 }
            else { bal -= 1 }
            if bal < 0 { return false }
        }
        return true
    }
}
