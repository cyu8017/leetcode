// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

#include <string.h>

int longestBalanced(char* s) {
    int n = (int)strlen(s), ans = 0;
    for (int i = 0; i < n; i++) {
        int cnt[26] = {0};
        int mx = 0, v = 0;
        for (int j = i; j < n; j++) {
            int c = s[j] - 'a';
            cnt[c]++;
            if (cnt[c] == 1) v++;
            if (cnt[c] > mx) mx = cnt[c];
            if (mx * v == j - i + 1) {
                if (j - i + 1 > ans) ans = j - i + 1;
            }
        }
    }
    return ans;
}
