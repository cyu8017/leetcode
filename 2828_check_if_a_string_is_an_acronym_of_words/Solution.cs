// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

using System.Collections.Generic;

public class Solution {
    public bool IsAcronym(IList<string> words, string s) {
        if (words.Count != s.Length) return false;
        for (int i = 0; i < words.Count; i++) {
            if (words[i].Length == 0 || words[i][0] != s[i]) return false;
        }
        return true;
    }
}
