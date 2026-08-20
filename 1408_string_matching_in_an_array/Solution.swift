// LeetCode 1408 - String Matching in an Array
// https://leetcode.com/problems/string-matching-in-an-array/

class Solution {
    func stringMatching(_ words: [String]) -> [String] {
        words.enumerated().compactMap { i, word in
            words.enumerated().contains { j, other in i != j && other.contains(word) } ? word : nil
        }
    }
}
