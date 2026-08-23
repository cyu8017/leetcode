// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

public class Solution {
    public bool CheckAlmostEquivalent(string word1, string word2) {
        int[] freq = new int[26];
        for (int i = 0; i < word1.Length; i++) {
            freq[word1[i] - 'a']++;
            freq[word2[i] - 'a']--;
        }
        foreach (int v in freq) if (v > 3 || v < -3) return false;
        return true;
    }
}
