// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

#include <stdlib.h>

static int cmp_seg(const void* a, const void* b) {
    int* const* pa = (int* const*)a; int* const* pb = (int* const*)b;
    return (*pa)[0] - (*pb)[0];
}

long long maximumCoins(int** coins, int coinsSize, int* coinsColSize, int k) {
    (void)coinsColSize;
    qsort(coins, coinsSize, sizeof(int*), cmp_seg);
    int n = coinsSize; long long ans = 0;
    for (int i = 0; i < n; i++) {
        long long sum = 0; int start = coins[i][0], end = start + k - 1;
        for (int j = i; j < n && coins[j][0] <= end; j++) {
            int l = coins[j][0], r = coins[j][1];
            if (r > end) r = end; if (l < start) l = start;
            if (l <= r) sum += (long long)(r - l + 1) * coins[j][2];
        }
        if (sum > ans) ans = sum;
    }
    for (int i = 0; i < n; i++) {
        long long sum = 0; int end = coins[i][1], start = end - k + 1;
        for (int j = 0; j <= i; j++) {
            int l = coins[j][0], r = coins[j][1];
            if (l < start) l = start; if (r > end) r = end;
            if (l <= r) sum += (long long)(r - l + 1) * coins[j][2];
        }
        if (sum > ans) ans = sum;
    }
    return ans;
}
