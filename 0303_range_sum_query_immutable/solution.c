// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

#include <stdlib.h>

typedef struct {
    int* prefix;
    int prefixSize;
} NumArray;

NumArray* numArrayCreate(int* nums, int numsSize) {
    NumArray* obj = (NumArray*)malloc(sizeof(NumArray));
    obj->prefixSize = numsSize + 1;
    obj->prefix = (int*)calloc((size_t)obj->prefixSize, sizeof(int));
    for (int index = 0; index < numsSize; index++) {
        obj->prefix[index + 1] = obj->prefix[index] + nums[index];
    }
    return obj;
}

int numArraySumRange(NumArray* obj, int left, int right) {
    return obj->prefix[right + 1] - obj->prefix[left];
}

void numArrayFree(NumArray* obj) {
    if (!obj) {
        return;
    }
    free(obj->prefix);
    free(obj);
}
