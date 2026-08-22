// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

#include <stdbool.h>
#include <stdlib.h>

bool findSubarrays(int* nums, int numsSize) {
    int cap = 256;
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    bool* used = (bool*)calloc((size_t)cap, sizeof(bool));
    int count = 0;
    for (int i = 0; i + 1 < numsSize; i++) {
        int s = nums[i] + nums[i + 1];
        for (int j = 0; j < count; j++) if (keys[j] == s) { free(keys); free(used); return true; }
        if (count >= cap) {
            cap *= 2;
            keys = (int*)realloc(keys, (size_t)cap * sizeof(int));
        }
        keys[count++] = s;
    }
    free(keys); free(used);
    return false;
}
