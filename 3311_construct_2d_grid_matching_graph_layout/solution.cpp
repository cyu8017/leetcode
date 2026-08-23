// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> constructGridLayout(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<int> deg(n);
        for (int i = 0; i < n; i++) deg[i] = (int)g[i].size();
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (deg[i] == 1) { start = i; break; }
            if (deg[i] == 2) start = i;
        }
        std::vector<char> vis(n, 0);
        std::vector<int> row;
        int cur = start, prev = -1;
        for (;;) {
            row.push_back(cur);
            vis[cur] = 1;
            int next = -1;
            for (int v : g[cur]) {
                if (v != prev && !vis[v] && deg[v] <= 3) {
                    next = v;
                    if (deg[v] < 4) break;
                }
            }
            if (next == -1) break;
            prev = cur;
            cur = next;
        }
        int width = (int)row.size();
        int height = width ? n / width : n;
        if (width == 0 || width * height != n) {
            for (int w = 1; w <= n; w++) {
                if (n % w == 0) { width = w; height = n / w; break; }
            }
        }
        std::vector<std::vector<int>> grid(height, std::vector<int>(width, 0));
        for (int i = 0; i < n; i++) grid[i / width][i % width] = i;
        return grid;
    }
};
