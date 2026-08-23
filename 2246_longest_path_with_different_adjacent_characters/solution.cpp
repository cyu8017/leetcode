// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

#include <vector>
#include <string>
#include <functional>
#include <algorithm>

class Solution {
public:
    int longestPath(std::vector<int>& parent, std::string s) {
        int n = (int)parent.size();
        std::vector<std::vector<int>> g(n);
        for (int i = 1; i < n; ++i) g[parent[i]].push_back(i);
        int ans = 1;
        std::function<int(int)> dfs = [&](int u) {
            int best1 = 0, best2 = 0;
            for (int v : g[u]) {
                int lenV = dfs(v);
                if (s[v] == s[u]) continue;
                if (lenV > best1) { best2 = best1; best1 = lenV; }
                else if (lenV > best2) best2 = lenV;
            }
            ans = std::max(ans, 1 + best1 + best2);
            return 1 + best1;
        };
        dfs(0);
        return ans;
    }
};
