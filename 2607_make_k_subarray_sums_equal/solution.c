// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int gcd(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

long long makeSubKSumEqual(int* arr, int arrSize, int k) {
    int n = arrSize;
    int g = gcd(n, k);
    long long ans = 0;
    for (int r = 0; r < g; r++) {
        int* group = (int*)malloc((size_t)(n / g + 1) * sizeof(int));
        int gc = 0;
        for (int i = r; i < n; i += g) group[gc++] = arr[i];
        qsort(group, (size_t)gc, sizeof(int), cmpInt);
        int med = group[gc / 2];
        for (int i = 0; i < gc; i++) {
            long long d = group[i] - med;
            if (d < 0) d = -d;
            ans += d;
        }
        free(group);
    }
    return ans;
}
