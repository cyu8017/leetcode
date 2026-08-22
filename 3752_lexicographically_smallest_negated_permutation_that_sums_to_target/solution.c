// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* lexicographicallySmallest(int n, long long target, int* returnSize) {
    long long total = (long long)n * (n + 1) / 2;
    if (target < -total || target > total || (total - target) % 2 != 0) {
        *returnSize = 0;
        return NULL;
    }
    long long remaining = (total - target) / 2;
    bool* negative = (bool*)calloc((size_t)(n + 1), sizeof(bool));
    for (int value = n; value >= 1; value--) {
        if ((long long)value <= remaining) {
            negative[value] = true;
            remaining -= value;
        }
    }
    int* answer = (int*)malloc((size_t)n * sizeof(int));
    int p = 0;
    for (int value = n; value >= 1; value--) if (negative[value]) answer[p++] = -value;
    for (int value = 1; value <= n; value++) if (!negative[value]) answer[p++] = value;
    free(negative);
    *returnSize = n;
    return answer;
}
