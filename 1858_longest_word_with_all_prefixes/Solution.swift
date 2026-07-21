// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

class Solution {
    func longestWord(_ words: [String]) -> String {
        let wordSet = Set(words)
        var best = ""

        for word in words {
            var prefix = word
            var valid = true
            while !prefix.isEmpty {
                if !wordSet.contains(prefix) {
                    valid = false
                    break
                }
                prefix.removeLast()
            }

            if valid && (word.count > best.count || (word.count == best.count && word < best)) {
                best = word
            }
        }

        return best
    }
}
