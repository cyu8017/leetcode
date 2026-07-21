// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution {
    func longestBeautifulSubstring(_ word: String) -> Int {
        let chars = Array(word)
        let vowels = Array("aeiou")
        var best = 0
        for start in 0..<chars.count where chars[start] == "a" {
            var counts = Array(repeating: 0, count: 5)
            for end in start..<chars.count {
                let current = chars[end]
                if end > start && current < chars[end - 1] { break }
                guard let idx = vowels.firstIndex(of: current) else { break }
                counts[idx] += 1
                if idx > 0 && counts[idx - 1] == 0 { break }
                if counts.allSatisfy({ $0 > 0 }) {
                    best = max(best, end - start + 1)
                }
            }
        }
        return best
    }
}
