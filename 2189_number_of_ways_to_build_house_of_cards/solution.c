// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

#include <stdlib.h>
#include <string.h>

int houseOfCards(int n) {
    int* dp = (int*)calloc((size_t)n + 1, sizeof(int));
    dp[0] = 1;
    for (int k = 1; 3 * k - 1 <= n; k++) {
        int cost = 3 * k - 1;
        for (int j = n; j >= cost; j--) dp[j] += dp[j - cost];
    }
    int ans = dp[n];
    free(dp);
    return ans;
}
