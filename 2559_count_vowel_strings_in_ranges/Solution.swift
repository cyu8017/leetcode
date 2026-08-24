// LeetCode 2559 - Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution {
    func vowelStrings(_ words: [String], _ queries: [[Int]]) -> [Int] {
        func isV(_ c: Character) -> Bool {
            c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
        }
        let n = words.count
        var pref = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            pref[i + 1] = pref[i]
            let w = Array(words[i])
            if !w.isEmpty && isV(w[0]) && isV(w[w.count - 1]) { pref[i + 1] += 1 }
        }
        return queries.map { pref[$0[1] + 1] - pref[$0[0]] }
    }
}
