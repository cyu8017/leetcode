// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

#include <algorithm>
#include <vector>

class Solution {
public:
    int numWays(int steps, int arrLen) {
        const int mod = 1000000007;
        const int width = std::min(arrLen, steps / 2 + 1);
        std::vector<long long> dp(width, 0);
        dp[0] = 1;
        for (int s = 0; s < steps; ++s) {
            std::vector<long long> nxt(width, 0);
            for (int i = 0; i < width; ++i) {
                nxt[i] = dp[i];
                if (i) {
                    nxt[i] = (nxt[i] + dp[i - 1]) % mod;
                }
                if (i + 1 < width) {
                    nxt[i] = (nxt[i] + dp[i + 1]) % mod;
                }
            }
            dp.swap(nxt);
        }
        return static_cast<int>(dp[0]);
    }
};
