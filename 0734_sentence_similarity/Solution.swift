// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

class Solution {
    func areSentencesSimilar(_ sentence1: [String], _ sentence2: [String], _ similarPairs: [[String]]) -> Bool {
        if sentence1.count != sentence2.count { return false }
        var pairs = Set<String>()
        for p in similarPairs {
            pairs.insert(p[0] + "#" + p[1])
            pairs.insert(p[1] + "#" + p[0])
        }
        for i in 0..<sentence1.count {
            if sentence1[i] != sentence2[i] && !pairs.contains(sentence1[i] + "#" + sentence2[i]) {
                return false
            }
        }
        return true
    }
}
