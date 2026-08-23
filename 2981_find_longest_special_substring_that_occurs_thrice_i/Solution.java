// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

class Solution {
    public int maximumLength(String s) {
        int n = s.length(), ans = -1;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (s.charAt(j) != s.charAt(i)) break;
                int len = j - i + 1;
                int cnt = 0;
                for (int k = 0; k + len <= n; k++) {
                    boolean ok = true;
                    for (int t = 0; t < len; t++) {
                        if (s.charAt(k + t) != s.charAt(i + t)) { ok = false; break; }
                    }
                    if (ok) cnt++;
                }
                if (cnt >= 3 && len > ans) ans = len;
            }
        }
        return ans;
    }
}
