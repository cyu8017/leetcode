// LeetCode 1455 - Check If A Word Occurs As A Prefix Of Any Word In A Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        var words = sentence.split(' ');
        for (int i = 0; i < words.length; i++)
            if (words[i].startsWith(searchWord)) return i + 1;
        return -1;
    }
}
