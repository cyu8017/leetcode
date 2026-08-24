// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

class Solution {
    func wordSubsets(_ words1: [String], _ words2: [String]) -> [String] {
        let a = Int(Character("a").asciiValue!)
        var need = Array(repeating: 0, count: 26)
        for w in words2 {
            var cnt = Array(repeating: 0, count: 26)
            for c in w { cnt[Int(c.asciiValue!) - a] += 1 }
            for i in 0..<26 { need[i] = max(need[i], cnt[i]) }
        }
        var ans = [String]()
        for w in words1 {
            var cnt = Array(repeating: 0, count: 26)
            for c in w { cnt[Int(c.asciiValue!) - a] += 1 }
            var ok = true
            for i in 0..<26 where cnt[i] < need[i] { ok = false; break }
            if ok { ans.append(w) }
        }
        return ans
    }
}
