// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

class Solution {
    func numMatchingSubseq(_ s: String, _ words: [String]) -> Int {
        var waiting = Array(repeating: [(Int, Int)](), count: 26)
        let a = Int(Character("a").asciiValue!)
        let wordChars = words.map { Array($0) }
        for i in 0..<words.count {
            let w = wordChars[i]
            waiting[Int(w[0].asciiValue!) - a].append((i, 0))
        }
        var ans = 0
        for ch in s {
            let idx = Int(ch.asciiValue!) - a
            let cur = waiting[idx]
            waiting[idx] = []
            for (wi, pos) in cur {
                let nxt = pos + 1
                if nxt == wordChars[wi].count {
                    ans += 1
                } else {
                    waiting[Int(wordChars[wi][nxt].asciiValue!) - a].append((wi, nxt))
                }
            }
        }
        return ans
    }
}
