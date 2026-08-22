// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

#include <stdlib.h>
#include <string.h>

int* platesBetweenCandles(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = (int)strlen(s);
    int* pref = (int*)calloc((size_t)n + 1, sizeof(int));
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    int last = -1;
    for (int i = 0; i < n; i++) {
        pref[i + 1] = pref[i];
        if (s[i] == '*') pref[i + 1]++;
        else last = i;
        left[i] = last;
    }
    last = -1;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '|') last = i;
        right[i] = last;
    }
    int* ans = (int*)calloc((size_t)queriesSize, sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int l = right[queries[i][0]], r = left[queries[i][1]];
        if (l != -1 && r != -1 && l < r) ans[i] = pref[r] - pref[l];
    }
    free(pref); free(left); free(right);
    *returnSize = queriesSize;
    return ans;
}
