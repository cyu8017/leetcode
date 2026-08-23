// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

#include <algorithm>
#include <array>
#include <string>

class Solution {
public:
    int minOperations(std::string s1, std::string s2) {
        const int infinity = 1000000000;
        std::array<int, 2> dp{0, infinity};
        int n = (int)s1.size();
        for (int i = 0; i < n; i++) {
            std::array<int, 2> next{infinity, infinity};
            for (int forcedZero = 0; forcedZero <= 1; forcedZero++) {
                if (dp[forcedZero] == infinity) continue;
                char current = s1[i];
                if (forcedZero == 1) current = '0';

                int direct = dp[forcedZero];
                if (current == '0' && s2[i] == '1') direct++;
                else if (current == '1' && s2[i] == '0') direct = infinity;
                next[0] = std::min(next[0], direct);

                if (i + 1 < n) {
                    int cost = dp[forcedZero] + 1;
                    if (current == '0') cost++;
                    if (s1[i + 1] == '0') cost++;
                    if (s2[i] == '1') cost++;
                    next[1] = std::min(next[1], cost);
                }
            }
            dp = next;
        }
        return dp[0] == infinity ? -1 : dp[0];
    }
};
