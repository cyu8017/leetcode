// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

using System.Collections.Generic;

public class Solution {
    public string[] FindOcurrences(string text, string first, string second) {
        string[] words = text.Split(' ');
        var ans = new List<string>();
        for (int i = 0; i < words.Length - 2; i++) {
            if (words[i] == first && words[i + 1] == second) {
                ans.Add(words[i + 2]);
            }
        }
        return ans.ToArray();
    }
}
