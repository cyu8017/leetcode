// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

public class Solution {
    public string TruncateSentence(string s, int k) {
        string[] words = s.Split(' ');
        return string.Join(" ", words, 0, k);
    }
}
