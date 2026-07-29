// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int shortestPathLength(std::vector<std::vector<int>>& graph) {
        int n = static_cast<int>(graph.size());
        int target = (1 << n) - 1;
        std::queue<std::tuple<int, int, int>> queue;
        std::unordered_set<long long> seen;
        for (int i = 0; i < n; ++i) {
            queue.push({i, 1 << i, 0});
            seen.insert((static_cast<long long>(i) << 20) | (1 << i));
        }
        while (!queue.empty()) {
            auto [node, mask, dist] = queue.front();
            queue.pop();
            if (mask == target) {
                return dist;
            }
            for (int nxt : graph[node]) {
                int nmask = mask | (1 << nxt);
                long long state = (static_cast<long long>(nxt) << 20) | nmask;
                if (!seen.count(state)) {
                    seen.insert(state);
                    queue.push({nxt, nmask, dist + 1});
                }
            }
        }
        return -1;
    }
};
