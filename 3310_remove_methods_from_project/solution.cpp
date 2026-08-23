// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> remainingMethods(int n, int k, std::vector<std::vector<int>>& invocations) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : invocations) g[e[0]].push_back(e[1]);
        std::vector<char> sus(n, 0);
        std::function<void(int)> dfs = [&](int u) {
            if (sus[u]) return;
            sus[u] = 1;
            for (int v : g[u]) dfs(v);
        };
        dfs(k);
        for (auto& e : invocations) {
            if (!sus[e[0]] && sus[e[1]]) {
                std::vector<int> ans(n);
                for (int i = 0; i < n; i++) ans[i] = i;
                return ans;
            }
        }
        std::vector<int> ans;
        for (int i = 0; i < n; i++) if (!sus[i]) ans.push_back(i);
        return ans;
    }
};
