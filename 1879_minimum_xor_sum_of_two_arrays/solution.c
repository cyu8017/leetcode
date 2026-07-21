// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

#include <stdlib.h>
#include <limits.h>

int minimumXORSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    int N = 1 << n;
    int* dp = (int*)malloc((size_t)N * sizeof(int));
    for (int i = 0; i < N; i++) dp[i] = INT_MAX / 2;
    dp[0] = 0;
    for (int mask = 0; mask < N; mask++) {
        int i = 0;
        int tmp = mask;
        while (tmp) {
            i += tmp & 1;
            tmp >>= 1;
        }
        if (i >= n) continue;
        for (int j = 0; j < n; j++) {
            if (mask & (1 << j)) continue;
            int next = mask | (1 << j);
            int cost = dp[mask] + (nums1[i] ^ nums2[j]);
            if (cost < dp[next]) dp[next] = cost;
        }
    }
    int answer = dp[N - 1];
    free(dp);
    return answer;
}
