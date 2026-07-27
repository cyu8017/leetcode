// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

#include <stdlib.h>

static void sift_up(int* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] >= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}

static void sift_down(int* h, int n, int i) {
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < n && h[l] > h[best]) best = l;
        if (r < n && h[r] > h[best]) best = r;
        if (best == i) break;
        int t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
}

int lastStoneWeight(int* stones, int stonesSize) {
    int* h = (int*)malloc((size_t)stonesSize * sizeof(int));
    int n = 0;
    for (int i = 0; i < stonesSize; i++) {
        h[n] = stones[i];
        sift_up(h, n);
        n++;
    }
    while (n > 1) {
        int a = h[0];
        h[0] = h[--n];
        sift_down(h, n, 0);
        int b = h[0];
        h[0] = h[--n];
        sift_down(h, n, 0);
        if (a != b) {
            h[n] = a - b;
            sift_up(h, n);
            n++;
        }
    }
    int ans = n ? h[0] : 0;
    free(h);
    return ans;
}
