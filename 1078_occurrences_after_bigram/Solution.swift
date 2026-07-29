// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

class Solution {
    func findOcurrences(_ text: String, _ first: String, _ second: String) -> [String] {
        let words = text.split(separator: " ").map(String.init)
        var ans: [String] = []
        if words.count < 3 { return ans }
        for i in 0..<(words.count - 2) {
            if words[i] == first && words[i + 1] == second {
                ans.append(words[i + 2])
            }
        }
        return ans
    }
}
