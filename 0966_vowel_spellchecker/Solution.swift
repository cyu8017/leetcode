// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

class Solution {
    func spellchecker(_ wordlist: [String], _ queries: [String]) -> [String] {
        let exact = Set(wordlist)
        var lowerMap = [String: String]()
        var vowelMap = [String: String]()
        func devowel(_ w: String) -> String {
            return String(w.lowercased().map { "aeiou".contains($0) ? "*" : $0 })
        }
        for w in wordlist {
            let low = w.lowercased()
            if lowerMap[low] == nil { lowerMap[low] = w }
            let dv = devowel(w)
            if vowelMap[dv] == nil { vowelMap[dv] = w }
        }
        return queries.map { q in
            if exact.contains(q) { return q }
            if let w = lowerMap[q.lowercased()] { return w }
            if let w = vowelMap[devowel(q)] { return w }
            return ""
        }
    }
}
