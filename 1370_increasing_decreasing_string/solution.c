// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

#include <stdlib.h>
#include <string.h>

char* sortString(char* s) {
    int cnt[26] = {0}, n = (int)strlen(s);
    for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
    char* out = (char*)malloc(n + 1);
    int len = 0;
    while (len < n) {
        for (int i = 0; i < 26; i++) if (cnt[i]) { out[len++] = 'a' + i; cnt[i]--; }
        for (int i = 25; i >= 0; i--) if (cnt[i]) { out[len++] = 'a' + i; cnt[i]--; }
    }
    out[n] = '\0';
    return out;
}
