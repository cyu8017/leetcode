// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

#include <string.h>

int minOperations(char* s1, char* s2) {
    const int infinity = 1000000000;
    int dp[2] = {0, infinity};
    int n = (int)strlen(s1);
    for (int i = 0; i < n; i++) {
        int next[2] = {infinity, infinity};
        for (int forcedZero = 0; forcedZero <= 1; forcedZero++) {
            if (dp[forcedZero] == infinity) continue;
            char current = s1[i];
            if (forcedZero == 1) current = '0';

            int direct = dp[forcedZero];
            if (current == '0' && s2[i] == '1') direct++;
            else if (current == '1' && s2[i] == '0') direct = infinity;
            if (direct < next[0]) next[0] = direct;

            if (i + 1 < n) {
                int cost = dp[forcedZero] + 1;
                if (current == '0') cost++;
                if (s1[i + 1] == '0') cost++;
                if (s2[i] == '1') cost++;
                if (cost < next[1]) next[1] = cost;
            }
        }
        dp[0] = next[0];
        dp[1] = next[1];
    }
    if (dp[0] == infinity) return -1;
    return dp[0];
}
