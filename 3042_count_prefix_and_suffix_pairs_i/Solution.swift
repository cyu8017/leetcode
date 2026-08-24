// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution {
    func countPrefixSuffixPairs(_ words: [String]) -> Int {
        var ans = 0
        for i in 0..<words.count {
            let s = words[i]
            for j in (i + 1)..<words.count {
                let t = words[j]
                if t.count >= s.count && t.hasPrefix(s) && t.hasSuffix(s) {
                    ans += 1
                }
            }
        }
        return ans
    }
}
