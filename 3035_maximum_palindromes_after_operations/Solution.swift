// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

class Solution {
    func maxPalindromesAfterOperations(_ words: [String]) -> Int {
        var s = 0, mask = 0
        let aVal = Int(Character("a").asciiValue!)
        for w in words {
            s += w.count
            for ch in w {
                mask ^= 1 << (Int(ch.asciiValue!) - aVal)
            }
        }
        s -= mask.nonzeroBitCount
        let words = words.sorted { $0.count < $1.count }
        var ans = 0
        for w in words {
            s -= w.count / 2 * 2
            if s < 0 { break }
            ans += 1
        }
        return ans
    }
}
