// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

#include <stdlib.h>
#include <string.h>

int* maxHammingDistances(int* nums, int numsSize, int m, int* returnSize) {
    int N = 1 << m;
    int* dist = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) dist[i] = -1;
    int* q = malloc(N * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 0; i < numsSize; i++) {
        dist[nums[i]] = 0;
        q[qt++] = nums[i];
    }
    for (int k = 1; qh < qt; k++) {
        int end = qt;
        while (qh < end) {
            int x = q[qh++];
            for (int i = 0; i < m; i++) {
                int y = x ^ (1 << i);
                if (dist[y] == -1) { dist[y] = k; q[qt++] = y; }
            }
        }
    }
    int mask = (1 << m) - 1;
    for (int i = 0; i < numsSize; i++) nums[i] = m - dist[nums[i] ^ mask];
    free(dist); free(q);
    *returnSize = numsSize;
    return nums;
}
