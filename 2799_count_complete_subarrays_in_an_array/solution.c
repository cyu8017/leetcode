// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int countCompleteSubarrays(int* nums, int numsSize) {
    bool present[2001] = {0};
    int need = 0;
    for (int i = 0; i < numsSize; i++) {
        if (!present[nums[i]]) { present[nums[i]] = true; need++; }
    }
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        bool seen[2001];
        memset(seen, 0, sizeof(seen));
        int cnt = 0;
        for (int j = i; j < numsSize; j++) {
            if (!seen[nums[j]]) { seen[nums[j]] = true; cnt++; }
            if (cnt == need) { ans += numsSize - j; break; }
        }
    }
    return ans;
}
