// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

class Solution {
    func toGoatLatin(_ sentence: String) -> String {
        let vowels: Set<Character> = ["a","e","i","o","u","A","E","I","O","U"]
        let words = sentence.split(separator: " ").map(String.init)
        var out = [String]()
        for (i, word) in words.enumerated() {
            var goat = ""
            if vowels.contains(word.first!) {
                goat = word + "ma"
            } else {
                goat = String(word.dropFirst()) + String(word.first!) + "ma"
            }
            goat += String(repeating: "a", count: i + 1)
            out.append(goat)
        }
        return out.joined(separator: " ")
    }
}
