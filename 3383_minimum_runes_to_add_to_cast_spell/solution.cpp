// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

#include <functional>
#include <vector>

class Solution {
public:
    int minRunesToAdd(int n, std::vector<int>& crystals, std::vector<int>& flowFrom, std::vector<int>& flowTo) {
        std::vector<std::vector<int>> g(n), rg(n);
        for (int i = 0; i < (int)flowFrom.size(); i++) {
            int a = flowFrom[i], b = flowTo[i];
            g[a].push_back(b);
            rg[b].push_back(a);
        }
        std::vector<char> vis(n);
        std::vector<int> order;
        std::function<void(int)> dfs1 = [&](int u) {
            vis[u] = 1;
            for (int v : g[u]) if (!vis[v]) dfs1(v);
            order.push_back(u);
        };
        for (int i = 0; i < n; i++) if (!vis[i]) dfs1(i);
        std::vector<int> comp(n, -1);
        int cid = 0;
        std::function<void(int)> dfs2 = [&](int u) {
            comp[u] = cid;
            for (int v : rg[u]) if (comp[v] == -1) dfs2(v);
        };
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            if (comp[u] == -1) {
                dfs2(u);
                cid++;
            }
        }
        std::vector<char> hasCrystal(cid);
        for (int c : crystals) hasCrystal[comp[c]] = 1;
        std::vector<int> indeg(cid);
        for (int u = 0; u < n; u++) {
            for (int v : g[u]) {
                if (comp[u] != comp[v]) indeg[comp[v]]++;
            }
        }
        int ans = 0;
        for (int i = 0; i < cid; i++) {
            if (indeg[i] == 0 && !hasCrystal[i]) ans++;
        }
        return ans;
    }
};
