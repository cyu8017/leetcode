// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

class Solution {
    func wordSquares(_ words: [String]) -> [[String]] {
        let sortedWords = words.sorted()
        let length = sortedWords[0].count
        var prefixMap: [String: [String]] = ["": sortedWords]
        for word in sortedWords {
            for index in word.indices {
                let prefix = String(word[word.startIndex...index])
                prefixMap[prefix, default: []].append(word)
            }
        }

        var squares: [[String]] = []
        var current: [String] = []

        func dfs(_ row: Int) {
            if row == length {
                squares.append(current)
                return
            }
            let prefix = current.map { String($0[$0.index($0.startIndex, offsetBy: row)]) }.joined()
            for candidate in prefixMap[prefix, default: []] {
                current.append(candidate)
                dfs(row + 1)
                current.removeLast()
            }
        }

        dfs(0)
        return squares
    }
}
