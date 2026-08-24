// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution {
    func repeatedCharacter(_ s: String) -> Character {
        var seen = [Bool](repeating: false, count: 26)
        for c in s {
            let i = Int(c.asciiValue! - 97)
            if seen[i] { return c }
            seen[i] = true
        }
        return Character(" ")
    }
}
