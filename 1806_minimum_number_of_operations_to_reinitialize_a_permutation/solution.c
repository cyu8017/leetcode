// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

#include <stdlib.h>
#include <string.h>

int reinitializePermutation(int n) {
    int* perm = (int*)malloc((size_t)n * sizeof(int));
    int* next = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) perm[i] = i;
    int operations = 0;
    while (1) {
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) next[i] = perm[i / 2];
            else next[i] = perm[n / 2 + (i - 1) / 2];
        }
        memcpy(perm, next, (size_t)n * sizeof(int));
        operations++;
        int ok = 1;
        for (int i = 0; i < n; i++) {
            if (perm[i] != i) {
                ok = 0;
                break;
            }
        }
        if (ok) {
            free(perm);
            free(next);
            return operations;
        }
    }
}
