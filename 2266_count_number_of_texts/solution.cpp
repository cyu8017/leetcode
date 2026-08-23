// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

#include <string>
#include <vector>

class Solution {
public:
    int countTexts(std::string pressedKeys) {
        const int mod = 1000000007;
        int n = (int)pressedKeys.size();
        std::vector<int> dp(n + 1);
        dp[0] = 1;
        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i - 1];
            int maxPress = (pressedKeys[i - 1] == '7' || pressedKeys[i - 1] == '9') ? 4 : 3;
            for (int j = 2; j <= maxPress && j <= i; ++j) {
                if (pressedKeys[i - j] != pressedKeys[i - 1]) break;
                dp[i] = (dp[i] + dp[i - j]) % mod;
            }
        }
        return dp[n];
    }
};
