// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    double maxProbability(int n, std::vector<std::vector<int>>& edges, std::vector<double>& succProb,
                          int start_node, int end_node) {
        std::vector<std::vector<std::pair<int, double>>> graph(n);
        for (int i = 0; i < static_cast<int>(edges.size()); ++i) {
            const int a = edges[i][0];
            const int b = edges[i][1];
            const double probability = succProb[i];
            graph[a].emplace_back(b, probability);
            graph[b].emplace_back(a, probability);
        }

        std::priority_queue<std::pair<double, int>> heap;
        heap.emplace(1.0, start_node);
        std::vector<double> best(n, 0.0);
        best[start_node] = 1.0;

        while (!heap.empty()) {
            const auto [probability, node] = heap.top();
            heap.pop();
            if (node == end_node) {
                return probability;
            }
            if (probability < best[node]) {
                continue;
            }
            for (const auto& [neighbor, edge_probability] : graph[node]) {
                const double candidate = probability * edge_probability;
                if (candidate > best[neighbor]) {
                    best[neighbor] = candidate;
                    heap.emplace(candidate, neighbor);
                }
            }
        }
        return 0.0;
    }
};
