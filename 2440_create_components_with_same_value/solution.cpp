// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

#include <functional>
#include <vector>

class Solution {
public:
    int componentValue(std::vector<int>& nums, std::vector<std::vector<int>>& edges) {
        int n = (int)nums.size();
        int total = 0;
        for (int x : nums) total += x;
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::function<int(int, int, int)> dfs = [&](int u, int p, int target) -> int {
            int sum = nums[u];
            for (int v : g[u]) {
                if (v == p) continue;
                int sub = dfs(v, u, target);
                if (sub < 0) return -1;
                sum += sub;
            }
            if (sum > target) return -1;
            if (sum == target) return 0;
            return sum;
        };
        for (int parts = n; parts >= 1; parts--) {
            if (total % parts != 0) continue;
            int target = total / parts;
            if (dfs(0, -1, target) == 0) return parts - 1;
        }
        return 0;
    }
};
