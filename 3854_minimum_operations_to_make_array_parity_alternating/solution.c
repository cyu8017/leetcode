// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

#include <stdlib.h>
#include <limits.h>

int* makeParityAlternating(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(2 * sizeof(int));
    if (numsSize == 1) { ans[0] = 0; ans[1] = 0; *returnSize = 2; return ans; }
    int mn = nums[0], mx = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    int bestc = INT_MAX, bestr = INT_MAX;
    for (int kk = 0; kk <= 1; kk++) {
        int cnt = 0, a = INT_MAX, b = INT_MIN;
        for (int i = 0; i < numsSize; i++) {
            int x = nums[i];
            if (((x - i) & 1) != kk) {
                cnt++;
                if (x == mn) x++;
                else if (x == mx) x--;
            }
            if (x < a) a = x;
            if (x > b) b = x;
        }
        int r = b - a; if (r < 1) r = 1;
        if (cnt < bestc || (cnt == bestc && r < bestr)) { bestc = cnt; bestr = r; }
    }
    ans[0] = bestc; ans[1] = bestr;
    *returnSize = 2;
    return ans;
}
