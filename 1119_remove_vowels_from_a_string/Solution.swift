// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution {
    func removeVowels(_ s: String) -> String {
        let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
        return String(s.filter { !vowels.contains($0) })
    }
}
