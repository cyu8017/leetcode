// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

#include <stdlib.h>
#include <string.h>

int minChanges(int* nums, int numsSize, int k) {
    int* freq = (int*)calloc((size_t)k * 1024, sizeof(int));
    int* size = (int*)calloc(k, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        freq[(i % k) * 1024 + nums[i]]++;
        size[i % k]++;
    }
    const int INF = 1000000000;
    int dp[256];
    int ndp[256];
    for (int j = 0; j < 256; j++) {
        dp[j] = INF;
    }
    dp[0] = 0;
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < 256; j++) {
            ndp[j] = INF;
        }
        for (int xv = 0; xv < 256; xv++) {
            int cost = size[i] - freq[i * 1024 + xv];
            for (int xo = 0; xo < 256; xo++) {
                if (dp[xo] == INF) {
                    continue;
                }
                int key = xo ^ xv;
                if (dp[xo] + cost < ndp[key]) {
                    ndp[key] = dp[xo] + cost;
                }
            }
        }
        memcpy(dp, ndp, sizeof(dp));
    }
    int ans = dp[0];
    free(freq);
    free(size);
    return ans;
}
