// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

public class Solution {
    public int MinStartingIndex(string s, string pattern) {
        int n = s.Length, m = pattern.Length;
        for (int i = 0; i + m <= n; i++) {
            int diff = 0;
            for (int j = 0; j < m; j++) {
                if (s[i + j] != pattern[j]) {
                    diff++;
                    if (diff > 1) break;
                }
            }
            if (diff <= 1) return i;
        }
        return -1;
    }
}
