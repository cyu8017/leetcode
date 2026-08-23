// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> findSubtreeSizes(std::vector<int>& parent, std::string s) {
        int n = (int)parent.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; i++) g[parent[i]].push_back(i);
        std::vector<int> newParent = parent;
        std::vector<int> last(26, -1);
        std::function<void(int)> dfs1 = [&](int u) {
            int c = s[u] - 'a';
            int prev = last[c];
            if (prev != -1) newParent[u] = prev;
            last[c] = u;
            for (int v : g[u]) dfs1(v);
            last[c] = prev;
        };
        dfs1(0);
        std::vector<std::vector<int>> ng(n);
        for (int i = 1; i < n; i++) ng[newParent[i]].push_back(i);
        std::vector<int> ans(n);
        std::function<int(int)> dfs2 = [&](int u) {
            int sz = 1;
            for (int v : ng[u]) sz += dfs2(v);
            return ans[u] = sz;
        };
        dfs2(0);
        return ans;
    }
};
