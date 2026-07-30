// LeetCode 1455 - Check If A Word Occurs As A Prefix Of Any Word In A Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

public class Solution {
    public int IsPrefixOfWord(string sentence, string searchWord) {
        var words = sentence.Split(' ');
        for (int i = 0; i < words.Length; i++)
            if (words[i].StartsWith(searchWord)) return i + 1;
        return -1;
    }
}
