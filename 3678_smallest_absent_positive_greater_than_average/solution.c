// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

#include <stdlib.h>
#include <string.h>

int smallestAbsent(int* nums, int numsSize) {
    int sum = 0;
    int mn = 0, mx = 0;
    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    int offset = mn < 0 ? -mn : 0;
    int span = mx + offset + 2;
    if (span < 2) span = 2;
    char* seen = (char*)calloc((size_t)(span + 5), 1);
    for (int i = 0; i < numsSize; i++) {
        int idx = nums[i] + offset;
        if (idx >= 0 && idx < span + 5) seen[idx] = 1;
    }
    int ans = sum / numsSize + 1;
    if (ans < 1) ans = 1;
    while (1) {
        int idx = ans + offset;
        if (idx < 0 || idx >= span + 5 || !seen[idx]) break;
        ans++;
    }
    free(seen);
    return ans;
}
