// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

class Solution {
    func findAllConcatenatedWordsInADict(_ words: [String]) -> [String] {
        let sorted = words.sorted { $0.count < $1.count }
        var wordSet = Set(sorted)
        var result: [String] = []

        func canForm(_ word: String, _ dictionary: Set<String>) -> Bool {
            if word.isEmpty { return true }
            let length = word.count
            var dp = Array(repeating: false, count: length + 1)
            dp[0] = true
            var end = 1
            while end <= length {
                var start = 0
                while start < end {
                    let startIndex = word.index(word.startIndex, offsetBy: start)
                    let endIndex = word.index(word.startIndex, offsetBy: end)
                    if dp[start] && dictionary.contains(String(word[startIndex..<endIndex])) {
                        dp[end] = true
                    }
                    start += 1
                }
                end += 1
            }
            return dp[length]
        }

        for word in sorted {
            wordSet.remove(word)
            if canForm(word, wordSet) {
                result.append(word)
            }
            wordSet.insert(word)
        }
        return result
    }
}
