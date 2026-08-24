// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

class Solution {
    func areSentencesSimilarTwo(_ sentence1: [String], _ sentence2: [String], _ similarPairs: [[String]]) -> Bool {
        if sentence1.count != sentence2.count { return false }
        var parent = [String: String]()
        func find(_ x: String) -> String {
            parent[x] = parent[x] ?? x
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]!]
                x = parent[x]!
            }
            return x
        }
        for p in similarPairs {
            parent[p[0]] = parent[p[0]] ?? p[0]
            parent[p[1]] = parent[p[1]] ?? p[1]
            parent[find(p[0])] = find(p[1])
        }
        for i in 0..<sentence1.count {
            if sentence1[i] != sentence2[i] && find(sentence1[i]) != find(sentence2[i]) {
                return false
            }
        }
        return true
    }
}
