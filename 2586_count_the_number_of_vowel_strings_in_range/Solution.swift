// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution {
    func vowelStrings(_ words: [String], _ left: Int, _ right: Int) -> Int {
        func isV(_ c: Character) -> Bool {
            c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
        }
        var ans = 0
        for i in left...right {
            let w = Array(words[i])
            if isV(w[0]) && isV(w[w.count - 1]) { ans += 1 }
        }
        return ans
    }
}
