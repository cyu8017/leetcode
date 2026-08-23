// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

using System;
using System.Collections.Generic;

public class Solution {
    public string LongestWord(string[] words) {
        Array.Sort(words);
        var built = new HashSet<string> { "" };
        string best = "";
        foreach (string word in words) {
            if (built.Contains(word.Substring(0, word.Length - 1))) {
                built.Add(word);
                if (word.Length > best.Length) best = word;
            }
        }
        return best;
    }
}
