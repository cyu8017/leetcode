// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

#include <string.h>

int minStartingIndex(char* s, char* pattern) {
    int n = (int)strlen(s), m = (int)strlen(pattern);
    for (int i = 0; i + m <= n; i++) {
        int diff = 0;
        for (int j = 0; j < m; j++) {
            if (s[i + j] != pattern[j]) {
                if (++diff > 1) break;
            }
        }
        if (diff <= 1) return i;
    }
    return -1;
}
