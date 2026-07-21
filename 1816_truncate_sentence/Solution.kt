// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

class Solution {
    fun truncateSentence(s: String, k: Int): String {
        return s.split(" ").take(k).joinToString(" ")
    }
}
