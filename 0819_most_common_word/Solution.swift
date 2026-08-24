// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

class Solution {
    func mostCommonWord(_ paragraph: String, _ banned: [String]) -> String {
        let bannedSet = Set(banned)
        var counts = [String: Int]()
        var word = ""
        var best = ""
        var bestCount = 0
        let text = paragraph + " "
        for ch in text {
            if ch.isLetter {
                word.append(ch.lowercased())
            } else if !word.isEmpty {
                if !bannedSet.contains(word) {
                    let c = (counts[word] ?? 0) + 1
                    counts[word] = c
                    if c > bestCount {
                        bestCount = c
                        best = word
                    }
                }
                word = ""
            }
        }
        return best
    }
}
