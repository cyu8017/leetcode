// LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution {
    fun isPrefixOfWord(sentence: String, searchWord: String): Int {
        sentence.split(" ").forEachIndexed { index, word ->
            if (word.startsWith(searchWord)) return index + 1
        }
        return -1
    }
}
