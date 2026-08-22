// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int find2709(int* parent, int x) {
    if (parent[x] != x) parent[x] = find2709(parent, parent[x]);
    return parent[x];
}

static void union2709(int* parent, int a, int b) {
    int ra = find2709(parent, a), rb = find2709(parent, b);
    if (ra != rb) parent[ra] = rb;
}

bool canTraverseAllPairs(int* nums, int numsSize) {
    if (numsSize == 1) return true;
    int mx = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int* parent = (int*)malloc((size_t)(mx + 1) * sizeof(int));
    for (int i = 0; i <= mx; i++) parent[i] = i;
    bool* has = (bool*)calloc((size_t)(mx + 1), sizeof(bool));
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) { free(parent); free(has); return false; }
        has[nums[i]] = true;
    }
    int* sieve = (int*)calloc((size_t)(mx + 1), sizeof(int));
    for (int i = 2; i <= mx; i++) {
        if (sieve[i] == 0) {
            for (int j = i; j <= mx; j += i) {
                if (sieve[j] == 0) sieve[j] = i;
                if (has[j]) union2709(parent, i, j);
            }
        }
    }
    int root = find2709(parent, nums[0]);
    bool ok = true;
    for (int i = 0; i < numsSize; i++)
        if (find2709(parent, nums[i]) != root) { ok = false; break; }
    free(parent); free(has); free(sieve);
    return ok;
}
