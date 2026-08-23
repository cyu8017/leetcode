// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

#include <algorithm>
#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long minCost(std::string s, std::vector<int>& cost) {
        int64_t tot = 0;
        std::unordered_map<char, int64_t> g;
        for (int i = 0; i < (int)cost.size(); i++) {
            tot += cost[i];
            g[s[i]] += cost[i];
        }
        int64_t ans = tot;
        for (auto& [_, x] : g) ans = std::min(ans, tot - x);
        return ans;
    }
};
