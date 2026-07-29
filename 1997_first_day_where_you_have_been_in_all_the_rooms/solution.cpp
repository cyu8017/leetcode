// LeetCode 1997 - First Day Where You Have Been in All the Rooms
#include <vector>

class Solution {
public:
    int firstDayBeenInAllRooms(std::vector<int>& nextVisit) {
        const int MOD = 1000000007;
        int n = (int)nextVisit.size();
        std::vector<long long> dp(n, 0);
        for (int i = 1; i < n; i++) {
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD;
            if (dp[i] < 0) dp[i] += MOD;
        }
        return (int)dp[n - 1];
    }
};
