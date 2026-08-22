// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

#include <stdlib.h>

static int lowerBoundGt(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] <= x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int kIncreasing(int* arr, int arrSize, int k) {
    int ans = 0;
    for (int start = 0; start < k; start++) {
        int seqCap = (arrSize - start + k - 1) / k;
        int* seq = (int*)malloc((size_t)seqCap * sizeof(int));
        int seqLen = 0;
        for (int i = start; i < arrSize; i += k) seq[seqLen++] = arr[i];
        int* tails = (int*)malloc((size_t)seqLen * sizeof(int));
        int tlen = 0;
        for (int i = 0; i < seqLen; i++) {
            int x = seq[i];
            int j = lowerBoundGt(tails, tlen, x);
            if (j == tlen) tails[tlen++] = x;
            else tails[j] = x;
        }
        ans += seqLen - tlen;
        free(seq);
        free(tails);
    }
    return ans;
}
