// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxA(int n) {
        std::vector<int> dp(n + 1);
        for (int i = 0; i <= n; ++i) {
            dp[i] = i;
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i - 2; ++j) {
                dp[i] = std::max(dp[i], dp[j] * (i - j - 1));
            }
        }
        return dp[n];
    }
};
