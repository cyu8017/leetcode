// LeetCode 0798 - Smallest Rotation with Highest Score
#include <stdlib.h>

int bestRotation(int* nums, int numsSize) {
    int* change = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) change[i] = 1;
    for (int i = 0; i < numsSize; i++) {
        int idx = (i - nums[i] + 1) % numsSize;
        if (idx < 0) idx += numsSize;
        change[idx]--;
    }
    for (int i = 1; i < numsSize; i++) change[i] += change[i - 1];
    int best = 0;
    for (int i = 1; i < numsSize; i++) if (change[i] > change[best]) best = i;
    free(change);
    return best;
}
