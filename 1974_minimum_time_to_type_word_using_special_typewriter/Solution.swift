// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution {
    func minTimeToType(_ word: String) -> Int {
        var cur = Character("a")
        var ans = 0
        for ch in word {
            let d = abs(Int(ch.asciiValue!) - Int(cur.asciiValue!))
            ans += min(d, 26 - d) + 1
            cur = ch
        }
        return ans
    }
}
