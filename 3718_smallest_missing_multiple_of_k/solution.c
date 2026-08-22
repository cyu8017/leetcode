// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

#include <string.h>
#include <stdbool.h>

int missingMultiple(int* nums, int numsSize, int k) {
    bool s[100001] = {0};
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= 0 && nums[i] <= 100000) s[nums[i]] = true;
    }
    for (int i = 1; ; i++) {
        int x = k * i;
        if (x > 100000 || !s[x]) return x;
    }
}
