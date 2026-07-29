// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

#include <algorithm>
#include <limits>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int networkDelayTime(std::vector<std::vector<int>>& times, int n, int k) {
        std::vector<std::vector<std::pair<int, int>>> graph(n + 1);
        for (const auto& edge : times) {
            graph[edge[0]].push_back({edge[1], edge[2]});
        }
        const int INF = std::numeric_limits<int>::max() / 4;
        std::vector<int> dist(n + 1, INF);
        dist[k] = 0;
        using Node = std::pair<int, int>;
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> heap;
        heap.push({0, k});
        while (!heap.empty()) {
            auto [d, node] = heap.top();
            heap.pop();
            if (d > dist[node]) {
                continue;
            }
            for (auto [nei, weight] : graph[node]) {
                int nd = d + weight;
                if (nd < dist[nei]) {
                    dist[nei] = nd;
                    heap.push({nd, nei});
                }
            }
        }
        int ans = *std::max_element(dist.begin() + 1, dist.end());
        return ans == INF ? -1 : ans;
    }
};
