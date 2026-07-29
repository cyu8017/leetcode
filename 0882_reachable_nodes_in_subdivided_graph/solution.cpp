// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

#include <algorithm>
#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int reachableNodes(std::vector<std::vector<int>>& edges, int maxMoves, int n) {
        std::vector<std::unordered_map<int, int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]][e[1]] = e[2];
            graph[e[1]][e[0]] = e[2];
        }
        std::priority_queue<std::pair<int, int>> pq;
        pq.push({maxMoves, 0});
        std::unordered_map<int, int> seen;
        while (!pq.empty()) {
            auto [moves, node] = pq.top();
            pq.pop();
            if (seen.count(node)) {
                continue;
            }
            seen[node] = moves;
            for (auto [nei, cnt] : graph[node]) {
                int remain = moves - cnt - 1;
                if (!seen.count(nei) && remain >= 0) {
                    pq.push({remain, nei});
                }
            }
        }
        int ans = static_cast<int>(seen.size());
        for (auto& e : edges) {
            int left = seen.count(e[0]) ? seen[e[0]] : 0;
            int right = seen.count(e[1]) ? seen[e[1]] : 0;
            ans += std::min(e[2], left + right);
        }
        return ans;
    }
};
