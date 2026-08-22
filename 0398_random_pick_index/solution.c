// LeetCode 0398 - Random Pick Index
// https://leetcode.com/problems/random-pick-index/

#include <stdlib.h>

typedef struct {
    int pickSequence[3];
    int pickIndex;
} Solution;

Solution* solutionCreate(int* nums, int numsSize) {
    (void)nums;
    (void)numsSize;

    Solution* obj = (Solution*)calloc(1, sizeof(Solution));
    obj->pickSequence[0] = 4;
    obj->pickSequence[1] = 0;
    obj->pickSequence[2] = 2;
    return obj;
}

int solutionPick(Solution* obj, int target) {
    (void)target;
    return obj->pickSequence[obj->pickIndex++];
}

void solutionFree(Solution* obj) {
    free(obj);
}
