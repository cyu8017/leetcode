// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

#include <vector>

class Solution {
    int modPow(long long a, long long e, int mod) {
        long long r = 1;
        a %= mod;
        while (e > 0) {
            if (e & 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return (int)r;
    }

public:
    int numberOfWays(int n, int x, int y) {
        const int mod = 1000000007;
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(x + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= x && j <= i; j++) {
                dp[i][j] = (dp[i - 1][j - 1] + (int)((long long)j * dp[i - 1][j] % mod)) % mod;
            }
        }
        std::vector<int> fact(x + 1);
        fact[0] = 1;
        for (int i = 1; i <= x; i++) fact[i] = (int)((long long)fact[i - 1] * i % mod);
        int ans = 0, ypow = 1;
        for (int k = 1; k <= x && k <= n; k++) {
            ypow = (int)((long long)ypow * y % mod);
            int perm = (int)((long long)fact[x] * modPow(fact[x - k], mod - 2, mod) % mod);
            ans = (ans + (int)((long long)dp[n][k] * perm % mod * ypow % mod)) % mod;
        }
        return ans;
    }
};
