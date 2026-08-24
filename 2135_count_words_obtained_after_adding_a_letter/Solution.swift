// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

class Solution {
    func wordCount(_ startWords: [String], _ targetWords: [String]) -> Int {
        func mask(_ w: String) -> Int {
            var m = 0
            for c in w { m |= 1 << Int(c.asciiValue! - 97) }
            return m
        }
        var have = Set<Int>()
        for w in startWords { have.insert(mask(w)) }
        var ans = 0
        for w in targetWords {
            let m = mask(w)
            let chars = Array(w)
            for i in 0..<chars.count {
                if have.contains(m ^ (1 << Int(chars[i].asciiValue! - 97))) { ans += 1; break }
            }
        }
        return ans
    }
}
