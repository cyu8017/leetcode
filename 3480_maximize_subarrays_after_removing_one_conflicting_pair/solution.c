// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

#include <stdlib.h>

long long maxSubarrays(int n, int** conflictingPairs, int conflictingPairsSize, int* conflictingPairsColSize) {
    (void)conflictingPairsColSize;
    int m = conflictingPairsSize;
    long long best = 0;
    for (int skip = 0; skip < m; skip++) {
        int* rightLimit = (int*)malloc((size_t)(n + 2) * sizeof(int));
        for (int i = 0; i < n + 2; i++) rightLimit[i] = n + 1;
        for (int i = 0; i < m; i++) {
            if (i == skip) continue;
            int a = conflictingPairs[i][0], b = conflictingPairs[i][1];
            if (a > b) { int t = a; a = b; b = t; }
            if (b < rightLimit[a]) rightLimit[a] = b;
        }
        int minRight = n + 1;
        long long cnt = 0;
        for (int l = n; l >= 1; l--) {
            if (rightLimit[l] < minRight) minRight = rightLimit[l];
            cnt += (long long)(minRight - l);
        }
        if (cnt > best) best = cnt;
        free(rightLimit);
    }
    return best;
}
