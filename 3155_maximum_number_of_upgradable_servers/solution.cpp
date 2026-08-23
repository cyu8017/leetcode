// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> maxUpgrades(std::vector<int>& count, std::vector<int>& upgrade,
                                 std::vector<int>& sell, std::vector<int>& money) {
        std::vector<int> ans;
        for (int i = 0; i < (int)count.size(); i++) {
            long long cnt = count[i];
            ans.push_back((int)std::min(cnt, (cnt * sell[i] + money[i]) / (upgrade[i] + sell[i])));
        }
        return ans;
    }
};
