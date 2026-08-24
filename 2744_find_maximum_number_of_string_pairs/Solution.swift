// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution {
    func maximumNumberOfStringPairs(_ words: [String]) -> Int {
        var freq: [String: Int] = [:]
        var ans = 0
        for w in words {
            let rev = String(w.reversed())
            let c = freq[rev, default: 0]
            if c > 0 {
                ans += 1
                freq[rev] = c - 1
            } else {
                freq[w, default: 0] += 1
            }
        }
        return ans
    }
}
