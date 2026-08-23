// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> g(3);
        for (int x : nums) g[x % 3].push_back(x);
        int ans = 0;
        for (int a = 0; a < 3; a++) {
            if (!g[a].empty()) {
                int x = g[a].back();
                g[a].pop_back();
                for (int b = 0; b < 3; b++) {
                    if (!g[b].empty()) {
                        int y = g[b].back();
                        g[b].pop_back();
                        int c = (3 - (a + b) % 3) % 3;
                        if (!g[c].empty()) {
                            int z = g[c].back();
                            ans = std::max(ans, x + y + z);
                        }
                        g[b].push_back(y);
                    }
                }
                g[a].push_back(x);
            }
        }
        return ans;
    }
};
