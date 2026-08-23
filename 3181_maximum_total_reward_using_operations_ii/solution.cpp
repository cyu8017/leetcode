// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

#include <vector>
#include <algorithm>
#include <bitset>

class Solution {
public:
    int maxTotalReward(std::vector<int>& rewardValues) {
        std::sort(rewardValues.begin(), rewardValues.end());
        rewardValues.erase(std::unique(rewardValues.begin(), rewardValues.end()), rewardValues.end());
        constexpr int N = 100001;
        std::bitset<N> f;
        f[0] = 1;
        for (int v : rewardValues) {
            std::bitset<N> mask = f;
            // keep only bits < v
            for (int i = v; i < N; i++) mask.reset(i);
            f |= (mask << v);
        }
        for (int i = N - 1; i >= 0; i--) if (f[i]) return i;
        return 0;
    }
};
