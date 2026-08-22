// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

#include <stdlib.h>
#include <string.h>

int maximumLength(int* nums, int numsSize, int k) {
    int* f = calloc(numsSize * (k + 1), sizeof(int));
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int h = 0; h <= k; h++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] == nums[j]) {
                    if (f[j * (k + 1) + h] > f[i * (k + 1) + h])
                        f[i * (k + 1) + h] = f[j * (k + 1) + h];
                } else if (h > 0) {
                    if (f[j * (k + 1) + h - 1] > f[i * (k + 1) + h])
                        f[i * (k + 1) + h] = f[j * (k + 1) + h - 1];
                }
            }
            f[i * (k + 1) + h]++;
        }
        if (f[i * (k + 1) + k] > ans) ans = f[i * (k + 1) + k];
    }
    free(f);
    return ans;
}
