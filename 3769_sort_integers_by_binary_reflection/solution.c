// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

#include <stdlib.h>

static int reflect(int x) {
    int y = 0;
    while (x != 0) {
        y = (y << 1) | (x & 1);
        x >>= 1;
    }
    return y;
}

static int cmpRef(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    int fx = reflect(x), fy = reflect(y);
    if (fx != fy) return fx - fy;
    return x - y;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortByReflection(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) ans[i] = nums[i];
    qsort(ans, (size_t)numsSize, sizeof(int), cmpRef);
    *returnSize = numsSize;
    return ans;
}
