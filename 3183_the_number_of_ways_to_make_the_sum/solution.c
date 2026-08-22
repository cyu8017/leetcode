// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

#include <stdlib.h>

int numberOfWays(int n) {
    const int mod = 1000000007;
    int coins[3] = {1, 2, 6};
    int* f = calloc(n + 1, sizeof(int));
    f[0] = 1;
    for (int c = 0; c < 3; c++)
        for (int j = coins[c]; j <= n; j++)
            f[j] = (f[j] + f[j - coins[c]]) % mod;
    int ans = f[n];
    if (n >= 4) ans = (ans + f[n - 4]) % mod;
    if (n >= 8) ans = (ans + f[n - 8]) % mod;
    free(f);
    return ans;
}
