// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

#include <stdlib.h>
#include <stdbool.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

bool* checkArithmeticSubarrays(int* nums, int numsSize, int* l, int lSize, int* r, int rSize, int* returnSize) {
    (void)numsSize; (void)rSize;
    bool* ans = (bool*)malloc((size_t)lSize * sizeof(bool));
    for (int qi = 0; qi < lSize; qi++) {
        int len = r[qi] - l[qi] + 1;
        int* tmp = (int*)malloc((size_t)len * sizeof(int));
        for (int i = 0; i < len; i++) tmp[i] = nums[l[qi] + i];
        qsort(tmp, (size_t)len, sizeof(int), cmpInt);
        bool ok = true;
        if (len >= 3) {
            int diff = tmp[1] - tmp[0];
            for (int i = 2; i < len; i++) {
                if (tmp[i] - tmp[i - 1] != diff) { ok = false; break; }
            }
        }
        ans[qi] = ok;
        free(tmp);
    }
    *returnSize = lSize;
    return ans;
}
