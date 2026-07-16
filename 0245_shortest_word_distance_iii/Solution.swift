// LeetCode 0245 - Shortest Word Distance III
// https://leetcode.com/problems/shortest-word-distance-iii/

class Solution {
    func shortestWordDistance(_ wordsDict: [String], _ word1: String, _ word2: String) -> Int {
        if word1 == word2 {
            var previous = -1
            var best = Int.max
            for (index, word) in wordsDict.enumerated() {
                if word == word1 {
                    if previous >= 0 {
                        best = min(best, index - previous)
                    }
                    previous = index
                }
            }
            return best
        }

        var index1 = -1
        var index2 = -1
        var best = Int.max
        for (index, word) in wordsDict.enumerated() {
            if word == word1 {
                index1 = index
                if index2 >= 0 {
                    best = min(best, index - index2)
                }
            }
            if word == word2 {
                index2 = index
                if index1 >= 0 {
                    best = min(best, index - index1)
                }
            }
        }
        return best
    }
}
