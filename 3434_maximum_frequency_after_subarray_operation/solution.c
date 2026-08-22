// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

#include <stdlib.h>

int maxFrequency(int* nums, int numsSize, int k) {
    int base = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] == k) base++;
    int ans = base;
    int* uniq = (int*)malloc(numsSize * sizeof(int)); int un = 0;
    for (int i = 0; i < numsSize; i++) {
        int f = 0; for (int j = 0; j < un; j++) if (uniq[j] == nums[i]) f = 1;
        if (!f) uniq[un++] = nums[i];
    }
    for (int vi = 0; vi < un; vi++) {
        int v = uniq[vi]; if (v == k) continue;
        int best = 0, cur = 0;
        for (int i = 0; i < numsSize; i++) {
            int delta = 0;
            if (nums[i] == v) delta = 1; else if (nums[i] == k) delta = -1;
            cur += delta; if (cur < 0) cur = 0; if (cur > best) best = cur;
        }
        if (base + best > ans) ans = base + best;
    }
    free(uniq);
    return ans;
}
