// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isPossible(int* nums, int numsSize) {
    if (numsSize == 0) return true;
    int minV = nums[0], maxV = nums[numsSize - 1];
    int span = maxV - minV + 3;
    int* freq = (int*)calloc((size_t)span, sizeof(int));
    int* tails = (int*)calloc((size_t)span, sizeof(int));
    for (int i = 0; i < numsSize; i++) freq[nums[i] - minV]++;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i] - minV;
        if (freq[x] == 0) continue;
        freq[x]--;
        if (x > 0 && tails[x - 1] > 0) {
            tails[x - 1]--;
            tails[x]++;
        } else if (x + 2 < span && freq[x + 1] > 0 && freq[x + 2] > 0) {
            freq[x + 1]--;
            freq[x + 2]--;
            tails[x + 2]++;
        } else {
            free(freq); free(tails);
            return false;
        }
    }
    free(freq); free(tails);
    return true;
}
