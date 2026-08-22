// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int* findKDistantIndices(int* nums, int numsSize, int key, int k, int* returnSize) {
    bool* mark = (bool*)calloc((size_t)numsSize, sizeof(bool));
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == key) {
            int l = i - k; if (l < 0) l = 0;
            int r = i + k; if (r >= numsSize) r = numsSize - 1;
            for (int j = l; j <= r; j++) mark[j] = true;
        }
    }
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    int an = 0;
    for (int i = 0; i < numsSize; i++) if (mark[i]) ans[an++] = i;
    free(mark);
    *returnSize = an;
    return ans;
}
