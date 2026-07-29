#include <vector>

class Solution {
public:
    int numberWays(std::vector<std::vector<int>>& hats) {
        const int mod = 1000000007;
        int people = (int)hats.size();
        std::vector<std::vector<int>> wearers(41);
        for (int person = 0; person < people; ++person)
            for (int hat : hats[person]) wearers[hat].push_back(person);
        std::vector<int> dp(1 << people, 0);
        dp[0] = 1;
        for (int hat = 1; hat <= 40; ++hat) {
            std::vector<int> nxt = dp;
            for (int mask = 0; mask < (1 << people); ++mask) {
                if (!dp[mask]) continue;
                for (int person : wearers[hat]) {
                    if (((mask >> person) & 1) == 0)
                        nxt[mask | (1 << person)] = (nxt[mask | (1 << person)] + dp[mask]) % mod;
                }
            }
            dp = std::move(nxt);
        }
        return dp[(1 << people) - 1];
    }
};
