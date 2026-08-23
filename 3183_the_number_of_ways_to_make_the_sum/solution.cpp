// LeetCode 3183 - The Number of Ways to Make the Sum
// https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

#include <vector>

class Solution {
public:
    int numberOfWays(int n) {
        const int mod = 1e9 + 7;
        int coins[] = {1, 2, 6};
        std::vector<int> f(n + 1);
        f[0] = 1;
        for (int x : coins) {
            for (int j = x; j <= n; j++) f[j] = (f[j] + f[j - x]) % mod;
        }
        int ans = f[n];
        if (n >= 4) ans = (ans + f[n - 4]) % mod;
        if (n >= 8) ans = (ans + f[n - 8]) % mod;
        return ans;
    }
};
