// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

public class Solution {
    public string MergeAlternately(string word1, string word2) {
        var out_ = new System.Text.StringBuilder();
        int i = 0;
        int j = 0;
        while (i < word1.Length || j < word2.Length) {
            if (i < word1.Length) {
                out_.Append(word1[i++]);
            }
            if (j < word2.Length) {
                out_.Append(word2[j++]);
            }
        }
        return out_.ToString();
    }
}
