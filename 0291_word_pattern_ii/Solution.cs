// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

using System.Collections.Generic;

public class Solution {
    public bool WordPatternMatch(string pattern, string s) {
        return Backtrack(pattern, s, 0, 0, new Dictionary<char, string>(), new Dictionary<string, char>());
    }

    private bool Backtrack(
        string pattern,
        string s,
        int patternIndex,
        int stringIndex,
        Dictionary<char, string> charToWord,
        Dictionary<string, char> wordToChar) {
        if (patternIndex == pattern.Length) {
            return stringIndex == s.Length;
        }
        char ch = pattern[patternIndex];
        if (charToWord.TryGetValue(ch, out string mappedWord)) {
            if (!s.StartsWith(mappedWord, stringIndex)) {
                return false;
            }
            return Backtrack(pattern, s, patternIndex + 1, stringIndex + mappedWord.Length, charToWord, wordToChar);
        }
        for (int end = stringIndex + 1; end <= s.Length; end++) {
            string word = s.Substring(stringIndex, end - stringIndex);
            if (wordToChar.ContainsKey(word)) {
                continue;
            }
            charToWord[ch] = word;
            wordToChar[word] = ch;
            if (Backtrack(pattern, s, patternIndex + 1, end, charToWord, wordToChar)) {
                return true;
            }
            charToWord.Remove(ch);
            wordToChar.Remove(word);
        }
        return false;
    }
}
