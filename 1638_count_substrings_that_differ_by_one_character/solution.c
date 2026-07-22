// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

#include <string.h>

int countSubstrings(char* s, char* t) {
    int ns = (int)strlen(s), nt = (int)strlen(t), ans = 0;
    for (int i = 0; i < ns; i++) {
        for (int j = 0; j < nt; j++) {
            int diff = 0;
            for (int k = 0; k < ns - i && k < nt - j; k++) {
                if (s[i + k] != t[j + k]) diff++;
                if (diff == 1) ans++;
                else if (diff > 1) break;
            }
        }
    }
    return ans;
}
