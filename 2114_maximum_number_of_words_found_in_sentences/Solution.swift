// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution {
    func mostWordsFound(_ sentences: [String]) -> Int {
        sentences.map { $0.split(separator: " ").count }.max() ?? 0
    }
}
