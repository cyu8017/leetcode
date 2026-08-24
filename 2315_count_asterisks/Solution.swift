// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

class Solution {
    func countAsterisks(_ s: String) -> Int {
        var ans = 0, inside = false
        for c in s {
            if c == "|" { inside.toggle() }
            else if c == "*" && !inside { ans += 1 }
        }
        return ans
    }
}
