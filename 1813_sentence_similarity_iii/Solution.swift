// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

class Solution {
    func areSentencesSimilar(_ sentence1: String, _ sentence2: String) -> Bool {
        let words1 = sentence1.split(separator: " ").map(String.init)
        let words2 = sentence2.split(separator: " ").map(String.init)
        let n1 = words1.count
        let n2 = words2.count
        var i = 0
        while i < n1 && i < n2 && words1[i] == words2[i] {
            i += 1
        }
        if i == n1 || i == n2 { return true }
        var j1 = n1 - 1
        var j2 = n2 - 1
        while j1 >= i && j2 >= i && words1[j1] == words2[j2] {
            j1 -= 1
            j2 -= 1
        }
        return j1 < i || j2 < i
    }
}
