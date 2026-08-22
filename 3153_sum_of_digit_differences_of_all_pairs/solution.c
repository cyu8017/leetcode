// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

#include <math.h>

long long sumDigitDifferences(int* nums, int numsSize) {
    int m = (int)floor(log10((double)nums[0])) + 1;
    long long ans = 0;
    for (int k = 0; k < m; k++) {
        int cnt[10] = {0};
        for (int i = 0; i < numsSize; i++) {
            cnt[nums[i] % 10]++;
            nums[i] /= 10;
        }
        for (int v = 0; v < 10; v++) ans += (long long)cnt[v] * (numsSize - cnt[v]);
    }
    return ans / 2;
}
