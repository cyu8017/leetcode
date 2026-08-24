// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

class Solution {
    fun isCircularSentence(sentence: String): Boolean {
        val n = sentence.length
        if (sentence[0] != sentence[n - 1]) return false
        for (i in 0 until n) {
            if (sentence[i] == ' ' && sentence[i - 1] != sentence[i + 1]) return false
        }
        return true
    }
}
