// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

using System.Text;

public class Solution {
    public string LargestMerge(string word1, string word2) {
        int i = 0;
        int j = 0;
        var out_ = new StringBuilder();
        while (i < word1.Length && j < word2.Length) {
            if (string.CompareOrdinal(word1, i, word2, j, int.MaxValue) > 0) {
                out_.Append(word1[i]);
                i++;
            } else {
                out_.Append(word2[j]);
                j++;
            }
        }
        out_.Append(word1, i, word1.Length - i);
        out_.Append(word2, j, word2.Length - j);
        return out_.ToString();
    }
}
