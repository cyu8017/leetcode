// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution {
    fun checkIfPangram(sentence: String): Boolean {
        return sentence.toSet().size == 26
    }
}
