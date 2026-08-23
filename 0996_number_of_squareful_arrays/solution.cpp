// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

#include <cmath>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int numSquarefulPerms(std::vector<int>& nums) {
        std::unordered_map<int, int> count;
        for (int x : nums) count[x]++;
        std::unordered_map<int, std::vector<int>> graph;
        for (auto& [a, _] : count) graph[a] = {};
        for (auto& [a, _] : count) {
            for (auto& [b, __] : count) {
                long long s = 1LL * a + b;
                long long r = (long long)std::llround(std::sqrt((long double)s));
                if (r * r == s) graph[a].push_back(b);
            }
        }
        int ans = 0;
        auto dfs = [&](auto&& self, int x, int remain) -> void {
            if (remain == 0) {
                ans++;
                return;
            }
            for (int y : graph[x]) {
                if (count[y]) {
                    count[y]--;
                    self(self, y, remain - 1);
                    count[y]++;
                }
            }
        };
        for (auto& [x, _] : count) {
            count[x]--;
            dfs(dfs, x, (int)nums.size() - 1);
            count[x]++;
        }
        return ans;
    }
};
