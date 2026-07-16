// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution {
    func findSubstring(_ s: String, _ words: [String]) -> [Int] {
        if words.isEmpty || s.isEmpty {
            return []
        }

        let chars = Array(s)
        let wordLen = words[0].count
        let wordCount = words.count
        var need: [String: Int] = [:]
        for word in words {
            need[word, default: 0] += 1
        }

        var result: [Int] = []

        for start in 0..<wordLen {
            var left = start
            var counts: [String: Int] = [:]
            var used = 0
            var right = start

            while right <= chars.count - wordLen {
                let startIndex = chars.index(chars.startIndex, offsetBy: right)
                let endIndex = chars.index(startIndex, offsetBy: wordLen)
                let word = String(chars[startIndex..<endIndex])

                if need[word] == nil {
                    counts.removeAll()
                    used = 0
                    left = right + wordLen
                    right += wordLen
                    continue
                }

                counts[word, default: 0] += 1
                used += 1

                while counts[word, default: 0] > need[word, default: 0] {
                    let leftStart = chars.index(chars.startIndex, offsetBy: left)
                    let leftEnd = chars.index(leftStart, offsetBy: wordLen)
                    let leftWord = String(chars[leftStart..<leftEnd])
                    counts[leftWord, default: 0] -= 1
                    used -= 1
                    left += wordLen
                }

                if used == wordCount {
                    result.append(left)
                }

                right += wordLen
            }
        }

        return result.sorted()
    }
}
