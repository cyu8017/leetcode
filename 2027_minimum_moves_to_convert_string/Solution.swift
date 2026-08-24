// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution {
    func minimumMoves(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 0, i = 0
        while i < chars.count {
            if chars[i] == "X" {
                ans += 1
                i += 3
            } else {
                i += 1
            }
        }
        return ans
    }
}
