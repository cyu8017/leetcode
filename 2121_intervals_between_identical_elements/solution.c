// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

#include <stdlib.h>

long long* getDistances(int* arr, int arrSize, int* returnSize) {
    // values up to 1e5
    int maxv = 0;
    for (int i = 0; i < arrSize; i++) if (arr[i] > maxv) maxv = arr[i];
    int* cnt = (int*)calloc((size_t)maxv + 1, sizeof(int));
    for (int i = 0; i < arrSize; i++) cnt[arr[i]]++;
    int** pos = (int**)calloc((size_t)maxv + 1, sizeof(int*));
    int* fill = (int*)calloc((size_t)maxv + 1, sizeof(int));
    for (int v = 0; v <= maxv; v++) if (cnt[v]) pos[v] = (int*)malloc((size_t)cnt[v] * sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        int v = arr[i];
        pos[v][fill[v]++] = i;
    }
    long long* ans = (long long*)calloc((size_t)arrSize, sizeof(long long));
    for (int v = 0; v <= maxv; v++) {
        int m = cnt[v];
        if (m == 0) continue;
        long long* pref = (long long*)calloc((size_t)m + 1, sizeof(long long));
        for (int i = 0; i < m; i++) pref[i + 1] = pref[i] + pos[v][i];
        for (int i = 0; i < m; i++) {
            int idx = pos[v][i];
            long long left = (long long)i * idx - pref[i];
            long long right = (pref[m] - pref[i + 1]) - (long long)(m - i - 1) * idx;
            ans[idx] = left + right;
        }
        free(pref);
        free(pos[v]);
    }
    free(cnt); free(pos); free(fill);
    *returnSize = arrSize;
    return ans;
}
