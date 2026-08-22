// LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

#include <stdlib.h>
#include <string.h>

int maximumLength(int* nums, int numsSize, int k) {
    int* f = calloc(k * k, sizeof(int));
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i] % k;
        for (int j = 0; j < k; j++) {
            int y = (j - x + k) % k;
            f[x * k + y] = f[y * k + x] + 1;
            if (f[x * k + y] > ans) ans = f[x * k + y];
        }
    }
    free(f);
    return ans;
}
