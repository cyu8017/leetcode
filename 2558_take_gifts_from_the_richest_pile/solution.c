// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

#include <stdlib.h>

static void siftDown(int* h, int n, int i) {
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < n && h[l] > h[best]) best = l;
        if (r < n && h[r] > h[best]) best = r;
        if (best == i) break;
        int t = h[i]; h[i] = h[best]; h[best] = t;
        i = best;
    }
}

long long pickGifts(int* gifts, int giftsSize, int k) {
    int* h = (int*)malloc((size_t)giftsSize * sizeof(int));
    for (int i = 0; i < giftsSize; i++) h[i] = gifts[i];
    for (int i = giftsSize / 2 - 1; i >= 0; i--) siftDown(h, giftsSize, i);
    int n = giftsSize;
    for (int i = 0; i < k; i++) {
        int x = h[0];
        int lo = 0, hi = x;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if ((long long)mid * mid <= x) lo = mid;
            else hi = mid - 1;
        }
        h[0] = lo;
        siftDown(h, n, 0);
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) ans += h[i];
    free(h);
    return ans;
}
