// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

class Solution {
    func finalString(_ s: String) -> String {
        var b: [Character] = []
        for c in s {
            if c == "i" { b.reverse() } else { b.append(c) }
        }
        return String(b)
    }
}
