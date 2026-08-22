// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

#include <stdlib.h>
#include <limits.h>

/* map int->int with small keys 1..100 */
int minOperations(int* nums, int numsSize) {
    int f[101];
    for (int i = 0; i <= 100; i++) f[i] = -1;
    f[nums[0]] = 0;
    for (int i = 1; i < numsSize; i++) {
        int x = nums[i];
        int g[101];
        for (int t = 0; t <= 100; t++) g[t] = -1;
        for (int pre = 1; pre <= 100; pre++) {
            if (f[pre] < 0) continue;
            int cur = (x + pre - 1) / pre * pre;
            for (; cur <= 100; cur += pre) {
                int val = f[pre] + (cur - x);
                if (g[cur] < 0 || g[cur] > val) g[cur] = val;
            }
        }
        for (int t = 0; t <= 100; t++) f[t] = g[t];
    }
    int ans = INT_MAX;
    for (int t = 1; t <= 100; t++) if (f[t] >= 0 && f[t] < ans) ans = f[t];
    return ans;
}
