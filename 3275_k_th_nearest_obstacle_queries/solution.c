// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

#include <stdlib.h>

static void swapI(int* a, int* b) { int t=*a;*a=*b;*b=t; }
static void upMax(int* h, int i) {
    while (i > 0) { int p=(i-1)/2; if (h[i] <= h[p]) break; swapI(&h[i], &h[p]); i=p; }
}
static void downMax(int* h, int n, int i) {
    for (;;) {
        int l=2*i+1,r=l+1,b=i;
        if (l<n && h[l]>h[b]) b=l;
        if (r<n && h[r]>h[b]) b=r;
        if (b==i) break;
        swapI(&h[i], &h[b]); i=b;
    }
}

int* resultsArray(int** queries, int queriesSize, int* queriesColSize, int k, int* returnSize) {
    (void)queriesColSize;
    int* h = (int*)malloc((size_t)(k + 5) * sizeof(int));
    int hn = 0;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int d = queries[i][0]; if (d < 0) d = -d;
        int y = queries[i][1]; if (y < 0) d += -y; else d += y;
        h[hn] = d; upMax(h, hn++);
        if (hn > k) { h[0] = h[--hn]; if (hn) downMax(h, hn, 0); }
        ans[i] = (hn < k) ? -1 : h[0];
    }
    free(h);
    *returnSize = queriesSize;
    return ans;
}
