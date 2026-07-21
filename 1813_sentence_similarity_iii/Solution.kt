// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

class Solution {
    fun areSentencesSimilar(sentence1: String, sentence2: String): Boolean {
        val words1 = sentence1.split(" ")
        val words2 = sentence2.split(" ")
        val n1 = words1.size
        val n2 = words2.size

        var i = 0
        while (i < n1 && i < n2 && words1[i] == words2[i]) i++
        if (i == n1 || i == n2) return true

        var j1 = n1 - 1
        var j2 = n2 - 1
        while (j1 >= i && j2 >= i && words1[j1] == words2[j2]) {
            j1--
            j2--
        }
        return j1 < i || j2 < i
    }
}
