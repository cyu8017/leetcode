// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

#include <stdlib.h>

static int* parent;
static int find(int x) {
    if (parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
}
static int cmpIntDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}
static int cmpIntAsc(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maxAlternatingSum(int* nums, int numsSize, int** swaps, int swapsSize, int* swapsColSize) {
    (void)swapsColSize;
    int n = numsSize;
    parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    for (int i = 0; i < swapsSize; i++) {
        int a = find(swaps[i][0]), b = find(swaps[i][1]);
        if (a != b) parent[a] = b;
    }
    int* rootOf = (int*)malloc((size_t)n * sizeof(int));
    int* roots = (int*)malloc((size_t)n * sizeof(int));
    int rn = 0;
    for (int i = 0; i < n; i++) {
        int r = find(i);
        rootOf[i] = r;
        int seen = 0;
        for (int j = 0; j < rn; j++) if (roots[j] == r) { seen = 1; break; }
        if (!seen) roots[rn++] = r;
    }
    int* arr = (int*)calloc((size_t)n, sizeof(int));
    for (int ri = 0; ri < rn; ri++) {
        int r = roots[ri];
        int* vals = (int*)malloc((size_t)n * sizeof(int));
        int* even = (int*)malloc((size_t)n * sizeof(int));
        int* odd = (int*)malloc((size_t)n * sizeof(int));
        int vn = 0, en = 0, on = 0;
        for (int i = 0; i < n; i++) if (rootOf[i] == r) {
            vals[vn++] = nums[i];
            if (i % 2 == 0) even[en++] = i; else odd[on++] = i;
        }
        qsort(vals, (size_t)vn, sizeof(int), cmpIntDesc);
        qsort(even, (size_t)en, sizeof(int), cmpIntAsc);
        qsort(odd, (size_t)on, sizeof(int), cmpIntAsc);
        int ei = 0;
        for (int t = 0; t < vn; t++) {
            int v = vals[t];
            if (ei < en) arr[even[ei]] = v;
            else arr[odd[ei - en]] = v;
            ei++;
        }
        free(vals); free(even); free(odd);
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) ans += arr[i]; else ans -= arr[i];
    }
    free(parent); free(rootOf); free(roots); free(arr);
    return ans;
}
