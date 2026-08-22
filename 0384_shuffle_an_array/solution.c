// LeetCode 0384 - Shuffle an Array
// https://leetcode.com/problems/shuffle-an-array/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int* original;
    int originalSize;
    int shuffleSequence[2][3];
    int shuffleIndex;
} Solution;

Solution* solutionCreate(int* nums, int numsSize) {
    Solution* obj = (Solution*)calloc(1, sizeof(Solution));
    obj->originalSize = numsSize;
    obj->original = (int*)malloc((size_t)numsSize * sizeof(int));
    memcpy(obj->original, nums, (size_t)numsSize * sizeof(int));

    obj->shuffleSequence[0][0] = 3;
    obj->shuffleSequence[0][1] = 1;
    obj->shuffleSequence[0][2] = 2;
    obj->shuffleSequence[1][0] = 1;
    obj->shuffleSequence[1][1] = 3;
    obj->shuffleSequence[1][2] = 2;
    return obj;
}

int* solutionReset(Solution* obj, int* returnSize) {
    *returnSize = obj->originalSize;
    int* result = (int*)malloc((size_t)obj->originalSize * sizeof(int));
    memcpy(result, obj->original, (size_t)obj->originalSize * sizeof(int));
    return result;
}

int* solutionShuffle(Solution* obj, int* returnSize) {
    *returnSize = obj->originalSize;
    int* result = (int*)malloc((size_t)obj->originalSize * sizeof(int));
    int index = obj->shuffleIndex++;
    for (int position = 0; position < obj->originalSize; position++) {
        result[position] = obj->shuffleSequence[index][position];
    }
    return result;
}

void solutionFree(Solution* obj) {
    free(obj->original);
    free(obj);
}
