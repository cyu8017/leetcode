// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

#include <stdlib.h>
#include <string.h>

int countTexts(char* pressedKeys) {
    const int mod = 1000000007;
    int n = (int)strlen(pressedKeys);
    int* dp = (int*)calloc((size_t)(n + 1), sizeof(int));
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i - 1];
        int maxPress = 3;
        if (pressedKeys[i - 1] == '7' || pressedKeys[i - 1] == '9') maxPress = 4;
        for (int j = 2; j <= maxPress && j <= i; j++) {
            if (pressedKeys[i - j] != pressedKeys[i - 1]) break;
            dp[i] = (dp[i] + dp[i - j]) % mod;
        }
    }
    int ans = dp[n];
    free(dp);
    return ans;
}
