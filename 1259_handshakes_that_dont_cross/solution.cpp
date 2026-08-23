// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

#include <vector>

class Solution {
public:
    int numberOfWays(int numPeople) {
        const int mod = 1000000007;
        std::vector<long long> dp(numPeople + 1, 0);
        dp[0] = 1;
        for (int people = 2; people <= numPeople; people += 2) {
            long long total = 0;
            for (int left = 0; left < people; left += 2) {
                total = (total + dp[left] * dp[people - 2 - left]) % mod;
            }
            dp[people] = total;
        }
        return static_cast<int>(dp[numPeople]);
    }
};
