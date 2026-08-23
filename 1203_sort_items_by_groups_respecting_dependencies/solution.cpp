// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> sortItems(int n, int m, std::vector<int>& group, std::vector<std::vector<int>>& beforeItems) {
        for (int i = 0; i < n; ++i) {
            if (group[i] == -1) {
                group[i] = m++;
            }
        }
        std::vector<std::vector<int>> itemGraph(n);
        std::vector<int> itemIndeg(n, 0);
        std::vector<std::unordered_set<int>> groupGraph(m);
        std::vector<int> groupIndeg(m, 0);
        for (int v = 0; v < n; ++v) {
            for (int u : beforeItems[v]) {
                itemGraph[u].push_back(v);
                ++itemIndeg[v];
                if (group[u] != group[v] && !groupGraph[group[u]].count(group[v])) {
                    groupGraph[group[u]].insert(group[v]);
                    ++groupIndeg[group[v]];
                }
            }
        }
        auto topo = [](const std::vector<std::vector<int>>& graph, std::vector<int> indeg) {
            std::queue<int> q;
            for (int i = 0; i < static_cast<int>(indeg.size()); ++i) {
                if (indeg[i] == 0) {
                    q.push(i);
                }
            }
            std::vector<int> order;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                order.push_back(u);
                for (int v : graph[u]) {
                    if (--indeg[v] == 0) {
                        q.push(v);
                    }
                }
            }
            if (static_cast<int>(order.size()) != static_cast<int>(graph.size())) {
                return std::vector<int>{};
            }
            return order;
        };
        std::vector<std::vector<int>> gAdj(m);
        for (int u = 0; u < m; ++u) {
            for (int v : groupGraph[u]) {
                gAdj[u].push_back(v);
            }
        }
        std::vector<int> items = topo(itemGraph, itemIndeg);
        std::vector<int> groups = topo(gAdj, groupIndeg);
        if (items.empty() || groups.empty()) {
            return {};
        }
        std::vector<std::vector<int>> buckets(m);
        for (int item : items) {
            buckets[group[item]].push_back(item);
        }
        std::vector<int> answer;
        for (int g : groups) {
            for (int item : buckets[g]) {
                answer.push_back(item);
            }
        }
        return answer;
    }
};
