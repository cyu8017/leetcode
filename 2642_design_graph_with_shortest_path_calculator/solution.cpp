// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

#include <queue>
#include <vector>

class Graph {
    struct Edge {
        int to, w;
    };
    std::vector<std::vector<Edge>> g;

public:
    Graph(int n, std::vector<std::vector<int>>& edges) : g(n) {
        for (auto& e : edges) g[e[0]].push_back({e[1], e[2]});
    }

    void addEdge(std::vector<int> edge) {
        g[edge[0]].push_back({edge[1], edge[2]});
    }

    int shortestPath(int node1, int node2) {
        int n = (int)g.size();
        std::vector<int> dist(n, 1 << 30);
        dist[node1] = 0;
        using Item = std::pair<int, int>;
        std::priority_queue<Item, std::vector<Item>, std::greater<Item>> h;
        h.push({0, node1});
        while (!h.empty()) {
            auto [d, u] = h.top();
            h.pop();
            if (u == node2) return d;
            if (d > dist[u]) continue;
            for (auto& e : g[u]) {
                int nd = d + e.w;
                if (nd < dist[e.to]) {
                    dist[e.to] = nd;
                    h.push({nd, e.to});
                }
            }
        }
        return -1;
    }
};
