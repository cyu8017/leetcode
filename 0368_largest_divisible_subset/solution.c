// LeetCode 0368 - Largest Divisible Subset
// https://leetcode.com/problems/largest-divisible-subset/

#include <stdlib.h>

static int compareInts(const void* left, const void* right) {
    return (*(const int*)left - *(const int*)right);
}

typedef struct {
    int* values;
    int count;
    int capacity;
} Chain;

static void chainInit(Chain* chain, int value) {
    chain->values = (int*)malloc(sizeof(int));
    chain->values[0] = value;
    chain->count = 1;
    chain->capacity = 1;
}

static void chainCopyFrom(Chain* chain, const Chain* source, int extraValue) {
    free(chain->values);
    chain->count = source->count + 1;
    chain->capacity = chain->count;
    chain->values = (int*)malloc((size_t)chain->capacity * sizeof(int));
    for (int index = 0; index < source->count; index++) {
        chain->values[index] = source->values[index];
    }
    chain->values[chain->count - 1] = extraValue;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* largestDivisibleSubset(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    qsort(nums, (size_t)numsSize, sizeof(int), compareInts);
    Chain* chains = (Chain*)malloc((size_t)numsSize * sizeof(Chain));
    Chain best = {NULL, 0, 0};

    for (int index = 0; index < numsSize; index++) {
        chainInit(&chains[index], nums[index]);
        for (int prevIndex = 0; prevIndex < index; prevIndex++) {
            int prev = nums[prevIndex];
            int num = nums[index];
            if (prev < num && num % prev == 0 && chains[prevIndex].count + 1 > chains[index].count) {
                chainCopyFrom(&chains[index], &chains[prevIndex], num);
            }
        }
        if (chains[index].count > best.count) {
            if (best.values != NULL) {
                free(best.values);
            }
            best = chains[index];
            chains[index].values = NULL;
            chains[index].count = 0;
        }
    }

    for (int index = 0; index < numsSize; index++) {
        free(chains[index].values);
    }
    free(chains);

    *returnSize = best.count;
    return best.values;
}
