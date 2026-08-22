// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool checkArray(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long* diff = (long long*)calloc(n + 1, sizeof(long long));
    long long cur = 0;
    for (int i = 0; i < n; i++) {
        cur += diff[i];
        long long need = nums[i] - cur;
        if (need < 0) { free(diff); return false; }
        if (need > 0) {
            if (i + k > n) { free(diff); return false; }
            cur += need;
            diff[i + k] -= need;
        }
    }
    free(diff);
    return true;
}
