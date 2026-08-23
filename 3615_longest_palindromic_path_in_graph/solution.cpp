// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

#include <algorithm>
#include <queue>
#include <set>
#include <string>
#include <vector>

class Solution {
    int expandPal(std::vector<std::vector<int>>& g, const std::string& label, int l, int r) {
        std::set<std::pair<int, int>> vis;
        struct State { int l, r, length; };
        std::queue<State> q;
        int len0 = (l != r) ? 2 : 1;
        q.push({l, r, len0});
        int best = len0;
        vis.insert({std::min(l, r), std::max(l, r)});
        while (!q.empty()) {
            auto cur = q.front();
            q.pop();
            for (int a : g[cur.l]) {
                for (int b : g[cur.r]) {
                    if (a == b || label[a] != label[b]) continue;
                    auto p = std::make_pair(std::min(a, b), std::max(a, b));
                    if (vis.count(p)) continue;
                    vis.insert(p);
                    int nl = cur.length + 2;
                    best = std::max(best, nl);
                    q.push({a, b, nl});
                }
            }
        }
        return best;
    }

public:
    int maxLen(int n, std::vector<std::vector<int>>& edges, std::string label) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = 1;
        for (int i = 0; i < n; i++) {
            ans = std::max(ans, expandPal(g, label, i, i));
            for (int j : g[i]) {
                if (i < j && label[i] == label[j]) ans = std::max(ans, expandPal(g, label, i, j));
            }
        }
        return ans;
    }
};
