// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

#include <stdlib.h>

typedef struct {
    int* nums;
    int numsSize;
    int* tree;
} NumArray;

static void add(NumArray* obj, int index, int delta) {
    while (index <= obj->numsSize) {
        obj->tree[index] += delta;
        index += index & -index;
    }
}

static int prefix(const NumArray* obj, int index) {
    int total = 0;
    while (index > 0) {
        total += obj->tree[index];
        index -= index & -index;
    }
    return total;
}

NumArray* numArrayCreate(int* nums, int numsSize) {
    NumArray* obj = (NumArray*)malloc(sizeof(NumArray));
    obj->numsSize = numsSize;
    obj->nums = (int*)malloc((size_t)numsSize * sizeof(int));
    obj->tree = (int*)calloc((size_t)(numsSize + 1), sizeof(int));
    for (int index = 0; index < numsSize; index++) {
        obj->nums[index] = nums[index];
        add(obj, index + 1, nums[index]);
    }
    return obj;
}

void numArrayUpdate(NumArray* obj, int index, int val) {
    int delta = val - obj->nums[index];
    obj->nums[index] = val;
    add(obj, index + 1, delta);
}

int numArraySumRange(NumArray* obj, int left, int right) {
    return prefix(obj, right + 1) - prefix(obj, left);
}

void numArrayFree(NumArray* obj) {
    if (!obj) {
        return;
    }
    free(obj->nums);
    free(obj->tree);
    free(obj);
}
