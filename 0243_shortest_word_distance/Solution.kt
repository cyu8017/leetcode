// LeetCode 0243 - Shortest Word Distance
// https://leetcode.com/problems/shortest-word-distance/

class Solution {
    fun shortestWordDistance(wordsDict: Array<String>, word1: String, word2: String): Int {
        var index1 = -1
        var index2 = -1
        var best = Int.MAX_VALUE
        for ((index, word) in wordsDict.withIndex()) {
            if (word == word1) {
                index1 = index
                if (index2 >= 0) {
                    best = minOf(best, index - index2)
                }
            }
            if (word == word2) {
                index2 = index
                if (index1 >= 0) {
                    best = minOf(best, index - index1)
                }
            }
        }
        return best
    }
}
