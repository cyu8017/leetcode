// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

public class Solution {
    public int MostWordsFound(string[] sentences) {
        int ans = 0;
        foreach (string s in sentences) {
            int c = 1;
            foreach (char ch in s) if (ch == ' ') c++;
            ans = Math.Max(ans, c);
        }
        return ans;
    }
}
