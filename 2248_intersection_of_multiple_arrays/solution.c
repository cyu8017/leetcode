// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

#include <stdlib.h>
#include <string.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* intersection(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    int freq[1001] = {0};
    for (int i = 0; i < numsSize; i++) {
        char seen[1001] = {0};
        for (int j = 0; j < numsColSize[i]; j++) {
            int x = nums[i][j];
            if (!seen[x]) {
                freq[x]++;
                seen[x] = 1;
            }
        }
    }
    int* ans = (int*)malloc(1001 * sizeof(int));
    int n = 0;
    for (int x = 1; x <= 1000; x++) {
        if (freq[x] == numsSize) ans[n++] = x;
    }
    *returnSize = n;
    return ans;
}
