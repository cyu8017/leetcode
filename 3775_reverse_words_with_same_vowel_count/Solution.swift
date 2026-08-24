// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

class Solution {
    private func calc(_ w: String) -> Int {
        var cnt = 0
        for c in w where "aeiou".contains(c) { cnt += 1 }
        return cnt
    }

    func reverseWords(_ s: String) -> String {
        let words = s.split { $0.isWhitespace }.map(String.init)
        let cnt = calc(words[0])
        var ans = words[0]
        if words.count > 1 {
            for i in 1..<words.count {
                var w = words[i]
                if calc(w) == cnt { w = String(w.reversed()) }
                ans += " " + w
            }
        }
        return ans
    }
}
