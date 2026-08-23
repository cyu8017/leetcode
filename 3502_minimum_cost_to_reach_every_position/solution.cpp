// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> minCosts(std::vector<int>& cost) {
        int n = (int)cost.size();
        std::vector<int> ans(n);
        int mi = cost[0];
        for (int i = 0; i < n; i++) {
            mi = std::min(mi, cost[i]);
            ans[i] = mi;
        }
        return ans;
    }
};
