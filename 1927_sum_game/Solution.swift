// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

class Solution {
    func sumGame(_ num: String) -> Bool {
        let chars = Array(num)
        let half = chars.count / 2
        func score(_ s: ArraySlice<Character>) -> Int {
            var q = 0, dig = 0
            for c in s {
                if c == "?" { q += 1 }
                else { dig += c.wholeNumberValue! }
            }
            return dig * 2 + q * 9
        }
        return score(chars[..<half]) != score(chars[half...])
    }
}
