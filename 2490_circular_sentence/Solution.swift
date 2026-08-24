// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

class Solution {
    func isCircularSentence(_ sentence: String) -> Bool {
        let s = Array(sentence)
        let n = s.count
        if s[0] != s[n - 1] { return false }
        for i in 0..<n {
            if s[i] == " " && s[i - 1] != s[i + 1] { return false }
        }
        return true
    }
}
