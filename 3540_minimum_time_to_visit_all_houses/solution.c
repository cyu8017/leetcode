// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

#include <stdlib.h>

long long minTotalTime(int* forward, int forwardSize, int* backward, int backwardSize, int* queries, int queriesSize) {
    (void)backwardSize;
    int n = forwardSize;
    int sumB = 0;
    for (int i = 0; i < n; i++) sumB += backward[i];
    int* pf = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* pb = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < n; i++) {
        pf[i + 1] = pf[i] + forward[i];
        pb[i + 1] = pb[i] + backward[i];
    }
    long long ans = 0;
    int pos = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int q = queries[qi];
        int r = 0;
        if (q < pos) r = pf[n];
        r += pf[q] - pf[pos];
        int l = 0;
        if (q > pos) l = sumB;
        l += pb[pos] - pb[q];
        ans += (l < r) ? l : r;
        pos = q;
    }
    free(pf); free(pb);
    return ans;
}
