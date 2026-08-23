// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

#include <algorithm>
#include <functional>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> minimumFlips(int n, std::vector<std::vector<int>>& edges, std::string start, std::string target) {
        std::vector<std::vector<std::pair<int, int>>> g(n);
        for (int i = 0; i < n - 1; i++) {
            int a = edges[i][0], b = edges[i][1];
            g[a].push_back({b, i});
            g[b].push_back({a, i});
        }
        std::vector<int> ans;
        std::function<bool(int, int)> dfs = [&](int a, int fa) {
            bool rev = start[a] != target[a];
            for (auto [b, i] : g[a]) {
                if (b != fa && dfs(b, a)) {
                    ans.push_back(i);
                    rev = !rev;
                }
            }
            return rev;
        };
        if (dfs(0, -1)) return {-1};
        std::sort(ans.begin(), ans.end());
        return ans;
    }
};
