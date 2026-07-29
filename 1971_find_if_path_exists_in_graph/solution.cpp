// LeetCode 1971 - Find if Path Exists in Graph
#include <vector>

class Solution {
public:
    bool validPath(int n, std::vector<std::vector<int>>& edges, int source, int destination) {
        if (source == destination) return true;
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<char> seen(n, 0);
        std::vector<int> stack = {source};
        seen[source] = 1;
        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            if (u == destination) return true;
            for (int v : g[u]) if (!seen[v]) { seen[v] = 1; stack.push_back(v); }
        }
        return false;
    }
};
