// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

#include <stdlib.h>
static int iabs(int x){return x<0?-x:x;}
static int cmp_abs(const void* a, const void* b){return iabs(*(const int*)a)-iabs(*(const int*)b);}
int* sortByAbsoluteValue(int* nums, int numsSize, int* returnSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_abs);
    *returnSize = numsSize;
    return nums;
}
