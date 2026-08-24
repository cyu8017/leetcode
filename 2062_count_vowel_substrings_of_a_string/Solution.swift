// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution {
    func countVowelSubstrings(_ word: String) -> Int {
        let chars = Array(word)
        var ans = 0
        for i in 0..<chars.count {
            var seen = Set<Character>()
            var j = i
            while j < chars.count && isVowel(chars[j]) {
                seen.insert(chars[j])
                if seen.count == 5 { ans += 1 }
                j += 1
            }
        }
        return ans
    }

    private func isVowel(_ c: Character) -> Bool {
        return c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
    }
}
