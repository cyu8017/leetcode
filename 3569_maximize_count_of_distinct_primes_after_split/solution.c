// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int* maximumCount(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int mx = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    for (int i = 0; i < queriesSize; i++) if (queries[i][1] > mx) mx = queries[i][1];
    bool* isP = (bool*)calloc((size_t)mx + 1, sizeof(bool));
    for (int i = 2; i <= mx; i++) isP[i] = true;
    for (int i = 2; i * i <= mx; i++) if (isP[i])
        for (int j = i * i; j <= mx; j += i) isP[j] = false;
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int* leftc = (int*)calloc((size_t)mx + 1, sizeof(int));
    int* rightc = (int*)calloc((size_t)mx + 1, sizeof(int));
    for (int qi = 0; qi < queriesSize; qi++) {
        nums[queries[qi][0]] = queries[qi][1];
        memset(leftc, 0, (size_t)(mx + 1) * sizeof(int));
        memset(rightc, 0, (size_t)(mx + 1) * sizeof(int));
        int leftDistinct = 0, rightDistinct = 0;
        for (int i = 0; i < numsSize; i++) {
            int v = nums[i];
            if (v <= mx && isP[v]) {
                if (rightc[v]++ == 0) rightDistinct++;
            }
        }
        int best = 0;
        for (int i = 0; i < numsSize - 1; i++) {
            int v = nums[i];
            if (v <= mx && isP[v]) {
                if (leftc[v]++ == 0) leftDistinct++;
                if (--rightc[v] == 0) rightDistinct--;
            }
            int cur = leftDistinct + rightDistinct;
            if (cur > best) best = cur;
        }
        ans[qi] = best;
    }
    free(isP); free(leftc); free(rightc);
    *returnSize = queriesSize;
    return ans;
}
