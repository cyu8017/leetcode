// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/


class Solution {
    func countWordOccurrences(_ chunks: [String], _ queries: [String]) -> [Int] {
        let s = Array(chunks.joined())
        let n = s.count
        var cnt = [String: Int]()
        var i = 0
        while i < n {
            if s[i] == " " || s[i] == "-" {
                i += 1
                continue
            }
            var j = i
            while j < n && s[j] != " " && (s[j] != "-" || (j + 1 < n && s[j + 1] != " " && s[j + 1] != "-")) {
                j += 1
            }
            let word = String(s[i..<j])
            cnt[word, default: 0] += 1
            i = j
        }
        return queries.map { cnt[$0, default: 0] }
    }
}
