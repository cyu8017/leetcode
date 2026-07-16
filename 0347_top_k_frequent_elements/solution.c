// LeetCode 0347 - Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int value;
    int count;
} Entry;

static int compareEntries(const void* a, const void* b) {
    const Entry* left = (const Entry*)a;
    const Entry* right = (const Entry*)b;
    return right->count - left->count;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    int capacity = numsSize > 0 ? numsSize : 1;
    Entry* entries = (Entry*)calloc((size_t)capacity, sizeof(Entry));
    int entryCount = 0;

    for (int index = 0; index < numsSize; index++) {
        int num = nums[index];
        int found = -1;
        for (int entryIndex = 0; entryIndex < entryCount; entryIndex++) {
            if (entries[entryIndex].value == num) {
                found = entryIndex;
                break;
            }
        }
        if (found >= 0) {
            entries[found].count += 1;
        } else {
            entries[entryCount].value = num;
            entries[entryCount].count = 1;
            entryCount += 1;
        }
    }

    qsort(entries, (size_t)entryCount, sizeof(Entry), compareEntries);

    *returnSize = k;
    int* result = (int*)malloc((size_t)k * sizeof(int));
    for (int index = 0; index < k; index++) {
        result[index] = entries[index].value;
    }

    free(entries);
    return result;
}
