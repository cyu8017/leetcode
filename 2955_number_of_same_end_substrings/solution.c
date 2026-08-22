// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

#include <stdlib.h>
#include <string.h>

int* sameEndSubstringCount(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = (int)strlen(s);
    int (*pref)[26] = calloc(n + 1, sizeof(*pref));
    for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) pref[i + 1][c] = pref[i][c];
        pref[i + 1][s[i] - 'a']++;
    }
    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        int l = queries[qi][0], r = queries[qi][1], total = 0;
        for (int c = 0; c < 26; c++) {
            int cnt = pref[r + 1][c] - pref[l][c];
            total += cnt * (cnt + 1) / 2;
        }
        ans[qi] = total;
    }
    free(pref);
    *returnSize = queriesSize;
    return ans;
}
