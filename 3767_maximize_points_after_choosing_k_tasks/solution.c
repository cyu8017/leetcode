// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

#include <stdlib.h>

static int* t1g; static int* t2g;
static int cmpIdx(const void* a, const void* b) {
    int i = *(const int*)a, j = *(const int*)b;
    int di = t1g[i] - t2g[i];
    int dj = t1g[j] - t2g[j];
    /* sort by (t1-t2) descending: return dj - di? Go: technique1[idx[j]]-technique2[idx[j]] < technique1[idx[i]]-technique2[idx[i]]
       so idx[i] should come before idx[j] if di > dj */
    return dj - di;
}

long long maxPoints(int* technique1, int technique1Size, int* technique2, int technique2Size, int k) {
    (void)technique2Size;
    int n = technique1Size;
    t1g = technique1; t2g = technique2;
    int* idx = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) idx[i] = i;
    qsort(idx, (size_t)n, sizeof(int), cmpIdx);
    long long ans = 0;
    for (int i = 0; i < n; i++) ans += technique2[i];
    for (int i = 0; i < k; i++) {
        int index = idx[i];
        ans -= technique2[index];
        ans += technique1[index];
    }
    for (int i = k; i < n; i++) {
        int index = idx[i];
        if (technique1[index] >= technique2[index]) {
            ans -= technique2[index];
            ans += technique1[index];
        }
    }
    free(idx);
    return ans;
}
