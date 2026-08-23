// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

#include <queue>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    long long shortestPath(int n, std::vector<std::vector<int>>& edges, std::string labels, int k) {
        std::vector<std::vector<std::pair<int, int>>> graph(n);
        for (auto& edge : edges) graph[edge[0]].push_back({edge[1], edge[2]});
        const long long infinity = (long long)((~0ULL) >> 2);
        std::vector<std::vector<long long>> distances(n, std::vector<long long>(k + 1, infinity));
        distances[0][1] = 0;
        using State = std::tuple<long long, int, int>;
        std::priority_queue<State, std::vector<State>, std::greater<State>> queue;
        queue.push({0, 0, 1});
        while (!queue.empty()) {
            auto [distance, node, run] = queue.top();
            queue.pop();
            if (distance != distances[node][run]) continue;
            if (node == n - 1) return distance;
            for (auto& [to, weight] : graph[node]) {
                int nextRun = 1;
                if (labels[node] == labels[to]) nextRun = run + 1;
                if (nextRun > k) continue;
                long long nextDistance = distance + weight;
                if (nextDistance < distances[to][nextRun]) {
                    distances[to][nextRun] = nextDistance;
                    queue.push({nextDistance, to, nextRun});
                }
            }
        }
        return -1;
    }
};
