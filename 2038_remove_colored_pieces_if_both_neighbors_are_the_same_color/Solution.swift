// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution {
    func winnerOfGame(_ colors: String) -> Bool {
        let chars = Array(colors)
        var a = 0, b = 0
        if chars.count < 3 { return false }
        for i in 1..<(chars.count - 1) {
            if chars[i - 1] == chars[i] && chars[i] == chars[i + 1] {
                if chars[i] == "A" { a += 1 }
                else { b += 1 }
            }
        }
        return a > b
    }
}
