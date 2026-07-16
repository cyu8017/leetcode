// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

using System.Collections.Generic;

public class Solution {
    public bool WordPattern(string pattern, string s) {
        string[] words = s.Split(' ');
        if (pattern.Length != words.Length) {
            return false;
        }
        Dictionary<char, string> charToWord = new();
        Dictionary<string, char> wordToChar = new();
        for (int index = 0; index < pattern.Length; index++) {
            char ch = pattern[index];
            string word = words[index];
            if (charToWord.TryGetValue(ch, out string? mappedWord)) {
                if (mappedWord != word) {
                    return false;
                }
            } else {
                if (wordToChar.ContainsKey(word)) {
                    return false;
                }
                charToWord[ch] = word;
                wordToChar[word] = ch;
            }
        }
        return true;
    }
}
