// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

#include <stdlib.h>
#include <stdbool.h>

int minOperations(int* nums, int numsSize) {
    bool* seen = (bool*)calloc(100001, sizeof(bool));
    for (int i = numsSize - 1; i >= 0; i--) {
        int x = nums[i];
        if (x >= 0 && x <= 100000) {
            if (seen[x]) {
                free(seen);
                return i / 3 + 1;
            }
            seen[x] = true;
        } else {
            /* fallback linear for out-of-range (unlikely) */
            for (int j = i + 1; j < numsSize; j++) {
                if (nums[j] == x) {
                    free(seen);
                    return i / 3 + 1;
                }
            }
        }
    }
    free(seen);
    return 0;
}
