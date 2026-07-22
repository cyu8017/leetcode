// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

#include <stdlib.h>

static long long comb(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k > n - k) k = n - k;
    long long r = 1;
    for (int i = 1; i <= k; i++) {
        r = r * (n - k + i) / i;
    }
    return r;
}

char* kthSmallestPath(int* destination, int destinationSize, int k) {
    (void)destinationSize;
    int v = destination[0], h = destination[1];
    int len = v + h;
    char* ans = (char*)malloc((size_t)len + 1);
    int pos = 0;
    while (h + v) {
        if (h) {
            long long count = comb(h + v - 1, v);
            if (k <= count) {
                ans[pos++] = 'H';
                h--;
                continue;
            }
            k -= (int)count;
        }
        ans[pos++] = 'V';
        v--;
    }
    ans[pos] = 0;
    return ans;
}
