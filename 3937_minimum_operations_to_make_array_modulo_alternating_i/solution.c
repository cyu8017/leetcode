// LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

#include <limits.h>

static int abs3937(int x) { return x < 0 ? -x : x; }
static int min3937(int a, int b) { return a < b ? a : b; }

int minOperations(int* nums, int numsSize, int k) {
    for (int i = 0; i < numsSize; i++) nums[i] %= k;
    int ans = INT_MAX;
    for (int x = 0; x < k; x++) {
        for (int y = 0; y < k; y++) {
            if (x == y) continue;
            int cnt = 0;
            for (int i = 0; i < numsSize; i++) {
                int target = (i & 1) ? y : x;
                int diff = abs3937(target - nums[i]);
                cnt += min3937(diff, k - diff);
            }
            if (cnt < ans) ans = cnt;
        }
    }
    return ans;
}
