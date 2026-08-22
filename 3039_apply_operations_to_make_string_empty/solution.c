// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

#include <stdlib.h>
#include <string.h>

char* lastNonEmptyString(char* s) {
    int cnt[26] = {0}, last[26] = {0}, mx = 0, n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        cnt[c]++;
        last[c] = i;
        if (cnt[c] > mx) mx = cnt[c];
    }
    char* ans = (char*)malloc((size_t)n + 1);
    int p = 0;
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        if (cnt[c] == mx && last[c] == i) ans[p++] = s[i];
    }
    ans[p] = '\0';
    return ans;
}
