// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

#include <unordered_set>
#include <vector>

class Solution {
public:
    bool isPossible(int n, std::vector<std::vector<int>>& edges) {
        std::vector<int> deg(n + 1);
        std::vector<std::unordered_set<int>> adj(n + 1);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            deg[u]++;
            deg[v]++;
            adj[u].insert(v);
            adj[v].insert(u);
        }
        std::vector<int> odd;
        for (int i = 1; i <= n; i++) if (deg[i] % 2 == 1) odd.push_back(i);
        if (odd.empty()) return true;
        if (odd.size() == 2) {
            int a = odd[0], b = odd[1];
            if (!adj[a].count(b)) return true;
            for (int i = 1; i <= n; i++) {
                if (i != a && i != b && !adj[a].count(i) && !adj[b].count(i)) return true;
            }
            return false;
        }
        if (odd.size() == 4) {
            int a = odd[0], b = odd[1], c = odd[2], d = odd[3];
            return (!adj[a].count(b) && !adj[c].count(d)) ||
                   (!adj[a].count(c) && !adj[b].count(d)) ||
                   (!adj[a].count(d) && !adj[b].count(c));
        }
        return false;
    }
};
