// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

#include <stdlib.h>

static void hup(int* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t; i = p;
    }
}
static int hpop(int* h, int* n) {
    int v = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = l + 1, s = i;
        if (l < *n && h[l] < h[s]) s = l;
        if (r < *n && h[r] < h[s]) s = r;
        if (s == i) break;
        int t = h[i]; h[i] = h[s]; h[s] = t; i = s;
    }
    return v;
}
static void hpush(int* h, int* n, int v) {
    h[(*n)++] = v; hup(h, *n - 1);
}

long long minEliminationTime(int* timeReq, int timeReqSize, int splitTime) {
    int* h = (int*)malloc((size_t)timeReqSize * sizeof(int));
    int hn = 0;
    for (int i = 0; i < timeReqSize; i++) hpush(h, &hn, timeReq[i]);
    while (hn > 1) {
        hpop(h, &hn);
        int b = hpop(h, &hn);
        hpush(h, &hn, b + splitTime);
    }
    long long ans = h[0];
    free(h);
    return ans;
}
