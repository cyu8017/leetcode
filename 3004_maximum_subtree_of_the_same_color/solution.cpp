// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    int maximumSubtreeSize(std::vector<std::vector<int>>& edges, std::vector<int>& colors) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<int> size(n);
        int ans = 0;
        std::function<bool(int, int)> dfs = [&](int a, int fa) -> bool {
            size[a] = 1;
            bool ok = true;
            for (int b : g[a]) {
                if (b != fa) {
                    bool t = dfs(b, a);
                    ok = ok && t && colors[a] == colors[b];
                    size[a] += size[b];
                }
            }
            if (ok) ans = std::max(ans, size[a]);
            return ok;
        };
        dfs(0, -1);
        return ans;
    }
};
