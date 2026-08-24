// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

class Solution {
    func trimTrailingVowels(_ s: String) -> String {
        var chars = Array(s)
        while !chars.isEmpty && isVowel(chars.last!) { chars.removeLast() }
        return String(chars)
    }

    private func isVowel(_ c: Character) -> Bool {
        return "aeiou".contains(c)
    }
}
