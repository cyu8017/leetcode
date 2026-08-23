// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

using System.Collections.Generic;

public class Solution {
    public IList<int> FindWordsContaining(string[] words, char x) {
        var ans = new List<int>();
        for (int i = 0; i < words.Length; i++) {
            foreach (char c in words[i]) {
                if (c == x) {
                    ans.Add(i);
                    break;
                }
            }
        }
        return ans;
    }
}
