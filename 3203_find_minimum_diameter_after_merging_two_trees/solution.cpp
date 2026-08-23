// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

#include <vector>
#include <algorithm>
#include <functional>

class Solution {
    int treeDiameter(std::vector<std::vector<int>>& edges) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = 0, a = 0;
        std::function<void(int, int, int)> dfs = [&](int i, int fa, int t) {
            for (int j : g[i]) if (j != fa) dfs(j, i, t + 1);
            if (ans < t) { ans = t; a = i; }
        };
        dfs(0, -1, 0);
        dfs(a, -1, 0);
        return ans;
    }
public:
    int minimumDiameterAfterMerge(std::vector<std::vector<int>>& edges1,
                                  std::vector<std::vector<int>>& edges2) {
        int d1 = treeDiameter(edges1), d2 = treeDiameter(edges2);
        return std::max({d1, d2, (d1 + 1) / 2 + (d2 + 1) / 2 + 1});
    }
};
