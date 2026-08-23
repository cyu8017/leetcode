// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maxTotalReward(std::vector<int>& rewardValues) {
        std::sort(rewardValues.begin(), rewardValues.end());
        int n = (int)rewardValues.size();
        std::vector<int> f(rewardValues[n - 1] << 1, -1);
        auto dfs = [&](auto&& self, int x) -> int {
            if (f[x] != -1) return f[x];
            auto it = std::upper_bound(rewardValues.begin(), rewardValues.end(), x);
            f[x] = 0;
            for (; it != rewardValues.end(); ++it) {
                f[x] = std::max(f[x], *it + self(self, x + *it));
            }
            return f[x];
        };
        return dfs(dfs, 0);
    }
};
