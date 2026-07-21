// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

public class Solution {
    public string SortSentence(string s) {
        string[] tokens = s.Split(' ');
        var ordered = new string[tokens.Length];
        foreach (string token in tokens) {
            int position = token[^1] - '1';
            ordered[position] = token.Substring(0, token.Length - 1);
        }
        return string.Join(" ", ordered);
    }
}
