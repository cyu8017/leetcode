// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

class Solution {
    func wordsAbbreviation(_ words: [String]) -> [String] {
        var prefixes = Array(repeating: 1, count: words.count)
        var changed = true
        while changed {
            changed = false
            var groups: [String: [Int]] = [:]
            for (index, word) in words.enumerated() {
                let key = abbreviate(word, prefixes[index])
                groups[key, default: []].append(index)
            }
            for indices in groups.values where indices.count > 1 {
                changed = true
                for index in indices {
                    prefixes[index] += 1
                }
            }
        }
        return words.enumerated().map { index, word in
            abbreviate(word, prefixes[index])
        }
    }

    private func abbreviate(_ word: String, _ prefix: Int) -> String {
        if prefix + 2 >= word.count {
            return word
        }
        let middle = word.count - prefix - 1
        let candidate = String(word.prefix(prefix)) + String(middle) + String(word.suffix(1))
        return candidate.count < word.count ? candidate : word
    }
}
