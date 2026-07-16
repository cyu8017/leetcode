// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int* values;
    int length;
} Sequence;

static Sequence* sequences;
static int sequenceCount;
static int sequenceCapacity;
static int* path;
static int pathLength;
static int pathCapacity;

static bool sequenceEqual(const Sequence* left, const Sequence* right) {
    if (left->length != right->length) {
        return false;
    }
    return memcmp(left->values, right->values, (size_t)left->length * sizeof(int)) == 0;
}

static bool containsSequence(const Sequence* target) {
    for (int index = 0; index < sequenceCount; index++) {
        if (sequenceEqual(&sequences[index], target)) {
            return true;
        }
    }
    return false;
}

static void addSequence(const int* values, int length) {
    Sequence candidate = {(int*)values, length};
    if (containsSequence(&candidate)) {
        return;
    }
    if (sequenceCount >= sequenceCapacity) {
        sequenceCapacity = sequenceCapacity == 0 ? 16 : sequenceCapacity * 2;
        sequences = (Sequence*)realloc(sequences, (size_t)sequenceCapacity * sizeof(Sequence));
    }
    int* copy = (int*)malloc((size_t)length * sizeof(int));
    memcpy(copy, values, (size_t)length * sizeof(int));
    sequences[sequenceCount].values = copy;
    sequences[sequenceCount].length = length;
    sequenceCount++;
}

static int compareSequences(const void* left, const void* right) {
    const Sequence* a = (const Sequence*)left;
    const Sequence* b = (const Sequence*)right;
    const int minLength = a->length < b->length ? a->length : b->length;
    for (int index = 0; index < minLength; index++) {
        if (a->values[index] != b->values[index]) {
            return a->values[index] - b->values[index];
        }
    }
    return a->length - b->length;
}

static void backtrack(const int* nums, int numsSize, int start) {
    if (pathLength >= 2) {
        addSequence(path, pathLength);
    }
    int used[201];
    memset(used, 0, sizeof(used));
    for (int index = start; index < numsSize; index++) {
        const int value = nums[index] + 100;
        if (used[value]) {
            continue;
        }
        if (pathLength > 0 && nums[index] < path[pathLength - 1]) {
            continue;
        }
        used[value] = 1;
        if (pathLength >= pathCapacity) {
            pathCapacity = pathCapacity == 0 ? 8 : pathCapacity * 2;
            path = (int*)realloc(path, (size_t)pathCapacity * sizeof(int));
        }
        path[pathLength++] = nums[index];
        backtrack(nums, numsSize, index + 1);
        pathLength--;
    }
}

int** findSubsequences(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    sequences = NULL;
    sequenceCount = 0;
    sequenceCapacity = 0;
    path = NULL;
    pathLength = 0;
    pathCapacity = 0;
    backtrack(nums, numsSize, 0);

    qsort(sequences, (size_t)sequenceCount, sizeof(Sequence), compareSequences);
    int** result = (int**)malloc((size_t)sequenceCount * sizeof(int*));
    int* columns = (int*)malloc((size_t)sequenceCount * sizeof(int));
    for (int index = 0; index < sequenceCount; index++) {
        result[index] = sequences[index].values;
        columns[index] = sequences[index].length;
    }
    free(sequences);
    free(path);
    *returnSize = sequenceCount;
    *returnColumnSizes = columns;
    return result;
}
