// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

public class Solution {
    public int MaximumLength(string s) {
        int n = s.Length, ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (s[j] != s[i]) break;
                string sub = s.Substring(i, j - i + 1);
                int cnt = 0, len = sub.Length;
                for (int k = 0; k + len <= n; k++) {
                    if (string.CompareOrdinal(s, k, sub, 0, len) == 0) cnt++;
                }
                if (cnt >= 3 && len > ans) ans = len;
            }
        }
        return ans;
    }
}
