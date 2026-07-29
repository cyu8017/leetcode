// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

#include <limits.h>
#include <stdlib.h>

static int cmpByRight(const void* a, const void* b) {
    const int* left = *(const int* const*)a;
    const int* right = *(const int* const*)b;
    return left[1] - right[1];
}

int findLongestChain(int** pairs, int pairsSize, int* pairsColSize) {
    (void)pairsColSize;
    qsort(pairs, (size_t)pairsSize, sizeof(int*), cmpByRight);
    int length = 0;
    int currentEnd = INT_MIN;
    for (int i = 0; i < pairsSize; i++) {
        if (pairs[i][0] > currentEnd) {
            length++;
            currentEnd = pairs[i][1];
        }
    }
    return length;
}
