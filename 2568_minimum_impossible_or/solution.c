// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

#include <stdbool.h>

int minImpossibleOR(int* nums, int numsSize) {
    for (int i = 1; ; i <<= 1) {
        bool found = false;
        for (int j = 0; j < numsSize; j++) {
            if (nums[j] == i) { found = true; break; }
        }
        if (!found) return i;
    }
}
