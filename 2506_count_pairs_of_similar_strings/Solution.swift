// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution {
    func similarPairs(_ words: [String]) -> Int {
        var freq = [Int: Int]()
        var ans = 0
        for w in words {
            var mask = 0
            for c in w {
                mask |= 1 << Int(c.asciiValue! - Character("a").asciiValue!)
            }
            ans += freq[mask, default: 0]
            freq[mask, default: 0] += 1
        }
        return ans
    }
}
