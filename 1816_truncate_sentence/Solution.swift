// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

class Solution {
    func truncateSentence(_ s: String, _ k: Int) -> String {
        return s.split(separator: " ").prefix(k).joined(separator: " ")
    }
}
