// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

using System.Linq;

public class Solution {
    public string ReorderSpaces(string text) {
        string[] words = text.Split(new[] { ' ' }, System.StringSplitOptions.RemoveEmptyEntries);
        int spaces = text.Count(ch => ch == ' ');
        if (words.Length == 1) return words[0] + new string(' ', spaces);
        int between = spaces / (words.Length - 1);
        int trailing = spaces % (words.Length - 1);
        return string.Join(new string(' ', between), words) + new string(' ', trailing);
    }
}
