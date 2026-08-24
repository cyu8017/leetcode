// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

class Solution {
    func uniqueMorseRepresentations(_ words: [String]) -> Int {
        let codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        let a = Int(Character("a").asciiValue!)
        var seen = Set<String>()
        for word in words {
            var code = ""
            for ch in word { code += codes[Int(ch.asciiValue!) - a] }
            seen.insert(code)
        }
        return seen.count
    }
}
