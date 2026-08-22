// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long putMarbles(int* weights, int weightsSize, int k) {
    int n = weightsSize;
    if (k == 1 || k == n) return 0;
    int* pair = (int*)malloc((size_t)(n - 1) * sizeof(int));
    for (int i = 0; i < n - 1; i++) pair[i] = weights[i] + weights[i + 1];
    qsort(pair, (size_t)(n - 1), sizeof(int), cmpInt);
    long long mn = 0, mx = 0;
    for (int i = 0; i < k - 1; i++) {
        mn += pair[i];
        mx += pair[n - 2 - i];
    }
    free(pair);
    return mx - mn;
}
