// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

#include <string.h>

int maximumLength(char* s) {
    int n = (int)strlen(s);
    int ans = -1;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (s[j] != s[i]) break;
            int len = j - i + 1;
            int cnt = 0;
            for (int k = 0; k + len <= n; k++) {
                int ok = 1;
                for (int t = 0; t < len; t++) {
                    if (s[k + t] != s[i + t]) { ok = 0; break; }
                }
                if (ok) cnt++;
            }
            if (cnt >= 3 && len > ans) ans = len;
        }
    }
    return ans;
}
