// LeetCode 3741 - Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumDistance(std::vector<int>& nums) {
        std::unordered_map<int, std::vector<int>> g;
        for (int i = 0; i < (int)nums.size(); i++) g[nums[i]].push_back(i);
        const int inf = 1 << 30;
        int ans = inf;
        for (auto& [_, ls] : g) {
            int m = (int)ls.size();
            for (int h = 0; h < m - 2; h++) {
                ans = std::min(ans, (ls[h + 2] - ls[h]) * 2);
            }
        }
        return ans == inf ? -1 : ans;
    }
};
