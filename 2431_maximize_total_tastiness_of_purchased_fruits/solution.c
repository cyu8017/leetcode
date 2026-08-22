// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

#include <stdlib.h>

int maxTastiness(int* price, int priceSize, int* tastiness, int tastinessSize, int maxAmount, int maxCoupons) {
    (void)tastinessSize;
    int n = priceSize;
    int** dp = (int**)malloc((size_t)(maxAmount + 1) * sizeof(int*));
    for (int i = 0; i <= maxAmount; i++) {
        dp[i] = (int*)malloc((size_t)(maxCoupons + 1) * sizeof(int));
        for (int j = 0; j <= maxCoupons; j++) dp[i][j] = -1 << 30;
    }
    dp[0][0] = 0;
    for (int i = 0; i < n; i++) {
        int p = price[i], t = tastiness[i];
        for (int a = maxAmount; a >= 0; a--) {
            for (int c = maxCoupons; c >= 0; c--) {
                if (dp[a][c] < 0) continue;
                if (a + p <= maxAmount && dp[a][c] + t > dp[a + p][c])
                    dp[a + p][c] = dp[a][c] + t;
                if (c + 1 <= maxCoupons && a + p / 2 <= maxAmount && dp[a][c] + t > dp[a + p / 2][c + 1])
                    dp[a + p / 2][c + 1] = dp[a][c] + t;
            }
        }
    }
    int ans = 0;
    for (int a = 0; a <= maxAmount; a++)
        for (int c = 0; c <= maxCoupons; c++)
            if (dp[a][c] > ans) ans = dp[a][c];
    for (int i = 0; i <= maxAmount; i++) free(dp[i]);
    free(dp);
    return ans;
}
