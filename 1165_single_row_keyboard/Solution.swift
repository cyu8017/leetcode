// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

class Solution {
    func calculateTime(_ keyboard: String, _ word: String) -> Int {
        var pos = [Character: Int]()
        for (i, ch) in keyboard.enumerated() { pos[ch] = i }
        var ans = 0, cur = 0
        for ch in word {
            let p = pos[ch]!
            ans += abs(p - cur)
            cur = p
        }
        return ans
    }
}
