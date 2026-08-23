// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int longestCycle(std::vector<int>& edges) {
        int n = (int)edges.size();
        std::vector<char> vis(n, 0);
        int ans = -1;
        for (int i = 0; i < n; i++) {
            if (vis[i]) continue;
            std::unordered_map<int, int> dist;
            int cur = i, step = 0;
            while (cur != -1 && !vis[cur]) {
                vis[cur] = 1;
                dist[cur] = step;
                cur = edges[cur];
                step++;
            }
            if (cur != -1) {
                auto it = dist.find(cur);
                if (it != dist.end()) {
                    int cycle = step - it->second;
                    if (cycle > ans) ans = cycle;
                }
            }
        }
        return ans;
    }
};
