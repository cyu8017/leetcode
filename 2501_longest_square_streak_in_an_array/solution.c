// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int longestSquareStreak(int* nums, int numsSize) {
    bool* set = (bool*)calloc(100001, sizeof(bool));
    for (int i = 0; i < numsSize; i++) if (nums[i] <= 100000) set[nums[i]] = true;
    int best = -1;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x > 100000 || !set[x]) continue;
        int length = 0;
        long long cur = x;
        while (cur <= 100000 && set[cur]) {
            length++;
            set[cur] = false;
            if (cur > 100000) break;
            cur = cur * cur;
        }
        if (length >= 2 && length > best) best = length;
    }
    free(set);
    return best;
}
