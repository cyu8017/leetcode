// LeetCode 0164 - Maximum Gap
#include <limits.h>
#include <stdlib.h>
int maximumGap(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    int low = nums[0], high = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < low) low = nums[i];
        if (nums[i] > high) high = nums[i];
    }
    if (low == high) return 0;
    int size = (high - low) / (numsSize - 1);
    if (size < 1) size = 1;
    int count = (high - low) / size + 1;
    int *mins = malloc(count * sizeof(int)), *maxs = malloc(count * sizeof(int));
    char* used = calloc(count, sizeof(char));
    for (int i = 0; i < count; ++i) mins[i] = INT_MAX, maxs[i] = INT_MIN;
    for (int i = 0; i < numsSize; ++i) {
        int j = (nums[i] - low) / size;
        if (nums[i] < mins[j]) mins[j] = nums[i];
        if (nums[i] > maxs[j]) maxs[j] = nums[i];
        used[j] = 1;
    }
    int best = 0, previous = low;
    for (int i = 0; i < count; ++i) if (used[i]) {
        if (mins[i] - previous > best) best = mins[i] - previous;
        previous = maxs[i];
    }
    free(mins); free(maxs); free(used);
    return best;
}