// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

class ValidWordAbbr {
    private var groups: [String: Set<String>]

    init(_ dictionary: [String]) {
        groups = [:]
        for word in dictionary {
            let key = ValidWordAbbr.abbreviate(word)
            groups[key, default: []].insert(word)
        }
    }

    func isUnique(_ word: String) -> Bool {
        let key = ValidWordAbbr.abbreviate(word)
        guard let words = groups[key] else {
            return true
        }
        return words.count == 1 && words.contains(word)
    }

    private static func abbreviate(_ word: String) -> String {
        if word.count <= 2 {
            return word
        }
        let first = word.first!
        let last = word.last!
        return "\(first)\(word.count - 2)\(last)"
    }
}
