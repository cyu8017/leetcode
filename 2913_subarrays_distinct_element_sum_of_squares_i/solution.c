// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

#include <stdbool.h>
#include <string.h>

int sumCounts(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        bool seen[101] = {false};
        int d = 0;
        for (int j = i; j < numsSize; j++) {
            if (!seen[nums[j]]) { seen[nums[j]] = true; d++; }
            ans += d * d;
        }
    }
    return ans;
}
