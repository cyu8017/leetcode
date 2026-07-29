#include <vector>

class Solution {
    std::vector<std::vector<int>> graph;
    std::vector<bool> hasApple;
    int visit(int node, int parent) {
        int cost = 0;
        for (int child : graph[node]) {
            if (child != parent) {
                int childCost = visit(child, node);
                if (childCost || hasApple[child]) cost += childCost + 2;
            }
        }
        return cost;
    }
public:
    int minTime(int n, std::vector<std::vector<int>>& edges, std::vector<bool>& hasApple_) {
        graph.assign(n, {});
        hasApple = hasApple_;
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        return visit(0, -1);
    }
};
