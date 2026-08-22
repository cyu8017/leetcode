// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

#include <stdlib.h>
#include <stdbool.h>

int centeredSubarrays(int* nums, int numsSize) {
    int n = numsSize, ans = 0;
    for (int i = 0; i < n; i++) {
        int* keys = (int*)malloc((size_t)(n - i + 1) * sizeof(int));
        int ksz = 0;
        int s = 0;
        for (int j = i; j < n; j++) {
            s += nums[j];
            bool found = false;
            for (int t = 0; t < ksz; t++) if (keys[t] == nums[j]) { found = true; break; }
            if (!found) keys[ksz++] = nums[j];
            for (int t = 0; t < ksz; t++) if (keys[t] == s) { ans++; break; }
        }
        free(keys);
    }
    return ans;
}
