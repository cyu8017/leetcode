// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution {
    public boolean checkAlmostEquivalent(String word1, String word2) {
        int[] freq = new int[26];
        for (int i = 0; i < word1.length(); i++) {
            freq[word1.charAt(i) - 'a']++;
            freq[word2.charAt(i) - 'a']--;
        }
        for (int v : freq) if (v > 3 || v < -3) return false;
        return true;
    }
}
