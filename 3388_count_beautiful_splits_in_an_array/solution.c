// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

#include <stdbool.h>

static bool eq_range(int* a, int* b, int len) {
    for (int i = 0; i < len; i++) if (a[i] != b[i]) return false;
    return true;
}

int beautifulSplits(int* nums, int numsSize) {
    int n = numsSize, ans = 0;
    for (int i = 1; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            int ok = 0;
            if (i <= j - i && eq_range(nums, nums + i, i)) ok = 1;
            if (!ok && j - i <= n - j && eq_range(nums + i, nums + j, j - i)) ok = 1;
            if (ok) ans++;
        }
    }
    return ans;
}
