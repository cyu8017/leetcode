// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

#include <limits.h>
#include <stdlib.h>

int minMoves(int* nums, int numsSize, int k) {
    long long* adjusted = (long long*)malloc(numsSize * sizeof(long long));
    int m = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            adjusted[m] = i - m;
            m++;
        }
    }
    long long* prefix = (long long*)malloc((m + 1) * sizeof(long long));
    prefix[0] = 0;
    for (int i = 0; i < m; i++) {
        prefix[i + 1] = prefix[i] + adjusted[i];
    }
    long long best = LLONG_MAX;
    for (int left = 0; left + k <= m; left++) {
        int right = left + k;
        int mid = left + k / 2;
        long long median = adjusted[mid];
        long long cost = median * (mid - left) - (prefix[mid] - prefix[left]);
        cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1);
        if (cost < best) {
            best = cost;
        }
    }
    free(adjusted);
    free(prefix);
    return (int)best;
}
