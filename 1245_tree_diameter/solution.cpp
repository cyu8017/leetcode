// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    int treeDiameter(std::vector<std::vector<int>>& edges) {
        if (edges.empty()) {
            return 0;
        }
        std::unordered_map<int, std::vector<int>> graph;
        for (const auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        auto farthest = [&](int start) {
            std::queue<std::pair<int, int>> q;
            std::unordered_set<int> seen{start};
            q.push({start, 0});
            std::pair<int, int> last{start, 0};
            while (!q.empty()) {
                last = q.front();
                q.pop();
                for (int v : graph[last.first]) {
                    if (!seen.count(v)) {
                        seen.insert(v);
                        q.push({v, last.second + 1});
                    }
                }
            }
            return last;
        };
        int endpoint = farthest(edges[0][0]).first;
        return farthest(endpoint).second;
    }
};
