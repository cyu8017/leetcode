// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

#include <functional>
#include <set>
#include <vector>

class Solution {
public:
    int rootCount(std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& guesses, int k) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::set<std::pair<int, int>> guessSet;
        for (auto& gu : guesses) guessSet.insert({gu[0], gu[1]});
        std::function<int(int, int)> dfs1 = [&](int u, int p) {
            int cnt = 0;
            for (int v : g[u]) {
                if (v == p) continue;
                if (guessSet.count({u, v})) cnt++;
                cnt += dfs1(v, u);
            }
            return cnt;
        };
        int base = dfs1(0, -1);
        int ans = 0;
        std::function<void(int, int, int)> dfs2 = [&](int u, int p, int cur) {
            if (cur >= k) ans++;
            for (int v : g[u]) {
                if (v == p) continue;
                int nxt = cur;
                if (guessSet.count({u, v})) nxt--;
                if (guessSet.count({v, u})) nxt++;
                dfs2(v, u, nxt);
            }
        };
        dfs2(0, -1, base);
        return ans;
    }
};
