// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

#include <stdlib.h>
#include <string.h>

static int cmp_asc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

static int n3533, k3533, *nums3533, *pows3533;
static char* memo3533;
static char* seen3533;

static int dp3533(int mask, int mod) {
    if (mask == (1 << n3533) - 1) return mod == 0;
    int key = mask * k3533 + mod;
    if (seen3533[key]) return memo3533[key];
    seen3533[key] = 1;
    for (int i = 0; i < n3533; i++) {
        if (((mask >> i) & 1) == 0) {
            int nm = (mod * pows3533[i] + nums3533[i]) % k3533;
            if (dp3533(mask | (1 << i), nm)) { memo3533[key] = 1; return 1; }
        }
    }
    memo3533[key] = 0;
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* concatenatedDivisibility(int* nums, int numsSize, int k, int* returnSize) {
    n3533 = numsSize; k3533 = k;
    nums3533 = (int*)malloc((size_t)n3533 * sizeof(int));
    for (int i = 0; i < n3533; i++) nums3533[i] = nums[i];
    qsort(nums3533, (size_t)n3533, sizeof(int), cmp_asc);
    pows3533 = (int*)malloc((size_t)n3533 * sizeof(int));
    for (int i = 0; i < n3533; i++) {
        int p = 1, x = nums3533[i];
        if (x == 0) p = 10 % k;
        else while (x > 0) { p = p * 10 % k; x /= 10; }
        pows3533[i] = p;
    }
    int states = (1 << n3533) * k;
    memo3533 = (char*)calloc((size_t)states, 1);
    seen3533 = (char*)calloc((size_t)states, 1);
    if (!dp3533(0, 0)) {
        free(nums3533); free(pows3533); free(memo3533); free(seen3533);
        *returnSize = 0;
        return NULL;
    }
    int* ans = (int*)malloc((size_t)n3533 * sizeof(int));
    int mask = 0, mod = 0, ai = 0;
    while (mask != (1 << n3533) - 1) {
        for (int i = 0; i < n3533; i++) {
            if (((mask >> i) & 1) == 0) {
                int nm = (mod * pows3533[i] + nums3533[i]) % k;
                if (dp3533(mask | (1 << i), nm)) {
                    ans[ai++] = nums3533[i];
                    mask |= 1 << i;
                    mod = nm;
                    break;
                }
            }
        }
    }
    free(nums3533); free(pows3533); free(memo3533); free(seen3533);
    *returnSize = n3533;
    return ans;
}
