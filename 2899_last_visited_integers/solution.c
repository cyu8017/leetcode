// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

#include <stdlib.h>

int* lastVisitedIntegers(int* nums, int numsSize, int* returnSize) {
    int* seen = (int*)malloc(numsSize * sizeof(int));
    int sn = 0, k = 0;
    int* ans = (int*)malloc(numsSize * sizeof(int));
    int an = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != -1) { seen[sn++] = nums[i]; k = 0; }
        else {
            k++;
            if (k > sn) ans[an++] = -1;
            else ans[an++] = seen[sn - k];
        }
    }
    free(seen);
    *returnSize = an;
    return ans;
}
